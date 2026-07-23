from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoundItemPublic(BaseModel):
    id: int
    item_name: str
    description: str
    category: str
    found_location: str
    found_date: Optional[str] = None
    photo_url: Optional[str] = None
    created_at: datetime
    questions: list[str] = []  # just the question text, no answers

    class Config:
        orm_mode = True

class LostItemPublic(BaseModel):
    id: int
    item_name: str
    description: str
    category: str
    last_seen_location: str
    lost_date: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True