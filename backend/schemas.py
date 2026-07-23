from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr


# ---------- Organizer / Auth ----------

class OrganizerCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str  # "organizer" or "student" — lets the frontend know which dashboard to show


# ---------- Students ----------

class StudentCreate(BaseModel):
    """
    Used only by admins/organizers directly through /docs or curl to create
    student accounts — never exposed as a public signup form on the website.
    """
    username: str
    password: str
    name: str
    email: EmailStr
    faculty: Optional[str] = None
    grade: Optional[int] = None  # 1, 2, 3, 4


class StudentOut(BaseModel):
    id: int
    username: str
    name: str
    email: str
    faculty: Optional[str] = None
    grade: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


# ---------- Events ----------

class EventOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    team_size: int
    deadline: Optional[datetime] = None
    category: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------- Applications ----------
# Applications are now created from the logged-in student's own account —
# no manual name/email entry needed, so there's no ApplicationCreate body
# schema anymore (see /events/{event_id}/apply in main.py).

class ApplicationOut(BaseModel):
    id: int
    name: str
    email: str
    grade: Optional[str] = None
    faculty: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# ---------- Teams ----------

class TeamMemberOut(BaseModel):
    name: str
    email: str
    grade: Optional[str] = None
    faculty: Optional[str] = None


class TeamOut(BaseModel):
    team_number: int
    group_label: Optional[str] = None
    members: List[TeamMemberOut]