from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import LostItemPublic
import models
from pydantic import BaseModel

router = APIRouter()

class LostItemCreate(BaseModel):
    item_name: str
    description: str
    category: str
    last_seen_location: str
    contact_info: str

@router.post("/")
def create_lost_item(item: LostItemCreate, db: Session = Depends(get_db)):
    new_item = models.LostItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=list[LostItemPublic])
def list_lost_items(db: Session = Depends(get_db)):
    return db.query(models.LostItem).all()