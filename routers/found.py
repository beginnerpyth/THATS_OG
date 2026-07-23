from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
import shutil, uuid, json
from schemas import FoundItemPublic
from database import get_db
import models

router = APIRouter()

@router.post("/")
async def create_found_item(
    item_name: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    found_location: str = Form(...),
    contact_info: str = Form(...),
    verification_questions: str = Form(...),  # send as JSON string from frontend
    photo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    photo_url = None
    if photo:
        ext = photo.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        filepath = f"uploads/{filename}"
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(photo.file, buffer)
        photo_url = filepath

    new_item = models.FoundItem(
        item_name=item_name,
        description=description,
        category=category,
        found_location=found_location,
        contact_info=contact_info,
        photo_url=photo_url,
        verification_questions=json.loads(verification_questions)
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=list[FoundItemPublic])
def list_found_items(db: Session = Depends(get_db)):
    items = db.query(models.FoundItem).all()
    result = []
    for item in items:
        questions_only = [qa["q"] for qa in item.verification_questions]
        result.append({
            "id": item.id,
            "item_name": item.item_name,
            "description": item.description,
            "category": item.category,
            "found_location": item.found_location,
            "found_date": item.found_date,
            "photo_url": item.photo_url,
            "created_at": item.created_at,
            "questions": questions_only
        })
    return result