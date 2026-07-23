from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
from pydantic import BaseModel

router = APIRouter()

class ClaimSubmit(BaseModel):
    found_item_id: int
    claimant_contact: str
    submitted_answers: dict  # e.g. {"q1": "blue"}

@router.post("/")
def submit_claim(claim: ClaimSubmit, db: Session = Depends(get_db)):
    found_item = db.query(models.FoundItem).filter(models.FoundItem.id == claim.found_item_id).first()
    if not found_item:
        raise HTTPException(status_code=404, detail="Found item not found")

    correct = all(
        claim.submitted_answers.get(qa["q"], "").strip().lower() == qa["a"].strip().lower()
        for qa in found_item.verification_questions
    )

    new_claim = models.Claim(
        found_item_id=claim.found_item_id,
        claimant_contact=claim.claimant_contact,
        submitted_answers=claim.submitted_answers,
        is_verified=correct
    )
    db.add(new_claim)
    db.commit()

    if correct:
        return {"verified": True, "contact_info": found_item.contact_info}
    return {"verified": False, "message": "Answers incorrect"}