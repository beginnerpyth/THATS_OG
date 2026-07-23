from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base

class LostItem(Base):
    __tablename__ = "lost_items"
    id = Column(Integer, primary_key=True)
    item_name = Column(String(100))
    description = Column(Text)
    category = Column(String(50))
    last_seen_location = Column(String(100))
    lost_date = Column(Date)
    contact_info = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())

class FoundItem(Base):
    __tablename__ = "found_items"
    id = Column(Integer, primary_key=True)
    item_name = Column(String(100))
    description = Column(Text)
    category = Column(String(50))
    found_location = Column(String(100))
    found_date = Column(Date)
    contact_info = Column(String(100))
    photo_url = Column(String(255), nullable=True)
    verification_questions = Column(JSONB)
    created_at = Column(DateTime, server_default=func.now())

class Claim(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True)
    found_item_id = Column(Integer, ForeignKey("found_items.id"))
    claimant_contact = Column(String(100))
    submitted_answers = Column(JSONB)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())