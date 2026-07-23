from datetime import datetime
from typing import List, Optional

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload

import auth
import matching
import models
import schemas
from database import Base, SessionLocal, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Campus Event Team Matcher")

# For the hackathon, allow all origins. Tighten this to your actual frontend
# Render URL once you know it (e.g. allow_origins=["https://your-frontend.onrender.com"]).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

VALID_CATEGORIES = {"event", "club", "seminar", "research", "career"}


@app.get("/")
def root():
    return {"status": "ok", "message": "Campus Event Team Matcher API"}


# ============================================================
# ORGANIZER AUTH
# ============================================================
# NOTE: /organizer/register is an admin tool only. It is intentionally NOT
# called from any button on the website — organizer accounts are created by
# an admin directly via /docs or curl, then handed to the organizer.

@app.post("/organizer/register", response_model=schemas.Token)
def register_organizer(data: schemas.OrganizerCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Organizer).filter(models.Organizer.username == data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    organizer = models.Organizer(
        username=data.username,
        hashed_password=auth.hash_password(data.password),
    )
    db.add(organizer)
    db.commit()
    db.refresh(organizer)

    token = auth.create_access_token({"sub": organizer.username, "role": "organizer"})
    return {"access_token": token, "token_type": "bearer", "role": "organizer"}


@app.post("/organizer/login", response_model=schemas.Token)
def login_organizer(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    organizer = db.query(models.Organizer).filter(models.Organizer.username == form_data.username).first()
    if not organizer or not auth.verify_password(form_data.password, organizer.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = auth.create_access_token({"sub": organizer.username, "role": "organizer"})
    return {"access_token": token, "token_type": "bearer", "role": "organizer"}


# ============================================================
# STUDENT AUTH
# ============================================================
# NOTE: /student/register is also an admin tool only — same pattern as
# organizer registration. No public signup form exists on the website; the
# website only ever shows a login screen.

@app.post("/student/register", response_model=schemas.Token)
def register_student(data: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Student).filter(models.Student.username == data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    student = models.Student(
        username=data.username,
        hashed_password=auth.hash_password(data.password),
        name=data.name,
        email=data.email,
        faculty=data.faculty,
        grade=data.grade,
    )
    db.add(student)
    db.commit()
    db.refresh(student)

    token = auth.create_access_token({"sub": student.username, "role": "student"})
    return {"access_token": token, "token_type": "bearer", "role": "student"}


@app.post("/student/login", response_model=schemas.Token)
def login_student(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.username == form_data.username).first()
    if not student or not auth.verify_password(form_data.password, student.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = auth.create_access_token({"sub": student.username, "role": "student"})
    return {"access_token": token, "token_type": "bearer", "role": "student"}


@app.get("/student/me", response_model=schemas.StudentOut)
def get_my_profile(student: models.Student = Depends(auth.get_current_student)):
    return student


# ============================================================
# EVENTS (events / clubs / seminars / research / career postings)
# ============================================================

@app.post("/events", response_model=schemas.EventOut)
async def create_event(
    title: str = Form(...),
    description: str = Form(""),
    team_size: int = Form(...),
    deadline: str = Form(None),
    category: str = Form("event"),  # "event" | "club" | "seminar" | "research" | "career"
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
    organizer: models.Organizer = Depends(auth.get_current_organizer),
):
    if category not in VALID_CATEGORIES:
        raise HTTPException(status_code=400, detail=f"category must be one of {sorted(VALID_CATEGORIES)}")

    image_bytes = await file.read() if file else None
    content_type = file.content_type if file else None

    deadline_dt = None
    if deadline:
        try:
            deadline_dt = datetime.fromisoformat(deadline)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid deadline format")

    event = models.Event(
        title=title,
        description=description,
        team_size=team_size,
        deadline=deadline_dt,
        category=category,
        image=image_bytes,
        image_content_type=content_type,
        organizer_id=organizer.id,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@app.get("/events", response_model=List[schemas.EventOut])
def list_events(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Event)
    if category:
        query = query.filter(models.Event.category == category)
    return query.order_by(models.Event.created_at.desc()).all()


@app.get("/events/{event_id}", response_model=schemas.EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.get("/events/{event_id}/image")
def get_event_image(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event or not event.image:
        raise HTTPException(status_code=404, detail="Image not found")
    return Response(content=event.image, media_type=event.image_content_type or "image/jpeg")


@app.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    organizer: models.Organizer = Depends(auth.get_current_organizer),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.organizer_id != organizer.id:
        raise HTTPException(status_code=403, detail="You can only delete your own events")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}


# ============================================================
# APPLICATIONS — student must be logged in; no manual name/email entry
# ============================================================

@app.post("/events/{event_id}/apply", response_model=schemas.ApplicationOut)
def apply_to_event(
    event_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(auth.get_current_student),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.deadline and datetime.utcnow() > event.deadline:
        raise HTTPException(status_code=400, detail="Applications are closed for this event")

    existing = (
        db.query(models.Application)
        .filter(
            models.Application.event_id == event_id,
            models.Application.student_id == student.id,
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="You have already applied to this event")

    application = models.Application(
        event_id=event_id,
        student_id=student.id,
        name=student.name,
        email=student.email,
        grade=str(student.grade) if student.grade else None,
        faculty=student.faculty,
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@app.get("/events/{event_id}/applications", response_model=List[schemas.ApplicationOut])
def list_applications(
    event_id: int,
    db: Session = Depends(get_db),
    organizer: models.Organizer = Depends(auth.get_current_organizer),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.organizer_id != organizer.id:
        raise HTTPException(status_code=403, detail="You can only view applications for your own events")

    return db.query(models.Application).filter(models.Application.event_id == event_id).all()


@app.get("/student/my-applications", response_model=List[schemas.ApplicationOut])
def my_applications(
    db: Session = Depends(get_db),
    student: models.Student = Depends(auth.get_current_student),
):
    """A student's own application history across all events."""
    return db.query(models.Application).filter(models.Application.student_id == student.id).all()


# ============================================================
# TEAM GENERATION (random) + organizer manual edits
# ============================================================

@app.post("/events/{event_id}/generate-teams")
def generate_teams(
    event_id: int,
    db: Session = Depends(get_db),
    organizer: models.Organizer = Depends(auth.get_current_organizer),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.organizer_id != organizer.id:
        raise HTTPException(status_code=403, detail="You can only generate teams for your own events")

    db.query(models.Team).filter(models.Team.event_id == event_id).delete()
    db.commit()

    applications = db.query(models.Application).filter(models.Application.event_id == event_id).all()
    if not applications:
        raise HTTPException(status_code=400, detail="No applications yet for this event")

    grouped = matching.create_random_teams(applications, event.team_size)

    for idx, group in enumerate(grouped, start=1):
        team = models.Team(event_id=event_id, team_number=idx)
        db.add(team)
        db.flush()
        for applicant in group:
            db.add(models.TeamMember(team_id=team.id, application_id=applicant.id))

    db.commit()
    return {"message": f"{len(grouped)} teams created", "team_count": len(grouped)}


@app.put("/teams/{team_id}/move-member/{application_id}")
def move_member_to_team(
    team_id: int,
    application_id: int,
    db: Session = Depends(get_db),
    organizer: models.Organizer = Depends(auth.get_current_organizer),
):
    """
    Lets an organizer manually move a student from whichever team they're
    currently on into a different team (e.g. after reviewing the random
    result). Frontend for this is a follow-up step.
    """
    target_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not target_team:
        raise HTTPException(status_code=404, detail="Target team not found")

    event = db.query(models.Event).filter(models.Event.id == target_team.event_id).first()
    if not event or event.organizer_id != organizer.id:
        raise HTTPException(status_code=403, detail="You can only edit teams for your own events")

    member = (
        db.query(models.TeamMember)
        .filter(models.TeamMember.application_id == application_id)
        .first()
    )
    if not member:
        raise HTTPException(status_code=404, detail="This applicant isn't currently on any team")

    member.team_id = team_id
    db.commit()
    return {"message": "Member moved successfully"}


@app.get("/events/{event_id}/teams", response_model=List[schemas.TeamOut])
def get_teams(event_id: int, db: Session = Depends(get_db)):
    teams = (
        db.query(models.Team)
        .options(joinedload(models.Team.members).joinedload(models.TeamMember.application))
        .filter(models.Team.event_id == event_id)
        .order_by(models.Team.team_number)
        .all()
    )

    result = []
    for team in teams:
        members = [
            schemas.TeamMemberOut(
                name=m.application.name,
                email=m.application.email,
                grade=m.application.grade,
                faculty=m.application.faculty,
            )
            for m in team.members
        ]
        result.append(schemas.TeamOut(team_number=team.team_number, group_label=team.group_label, members=members))
    return result


# ============================================================
# AUTOMATIC TEAM GENERATION AFTER DEADLINE
# ============================================================

def auto_generate_teams_for_expired_events():
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        expired_events = (
            db.query(models.Event)
            .filter(models.Event.deadline.isnot(None), models.Event.deadline <= now)
            .all()
        )

        for event in expired_events:
            already_has_teams = db.query(models.Team).filter(models.Team.event_id == event.id).first()
            if already_has_teams:
                continue

            applications = db.query(models.Application).filter(models.Application.event_id == event.id).all()
            if not applications:
                continue

            grouped = matching.create_random_teams(applications, event.team_size)
            for idx, group in enumerate(grouped, start=1):
                team = models.Team(event_id=event.id, team_number=idx)
                db.add(team)
                db.flush()
                for applicant in group:
                    db.add(models.TeamMember(team_id=team.id, application_id=applicant.id))

            db.commit()
    finally:
        db.close()


scheduler = BackgroundScheduler()


@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(auto_generate_teams_for_expired_events, "interval", seconds=30)
    scheduler.start()


@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()