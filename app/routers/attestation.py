from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/attestation", tags=["Attestation"])

@router.post("/", response_model=schemas.AttestationOut)
def create_attestation(attestation: schemas.AttestationCreate, db: Session = Depends(get_db)):
    db_att = models.Attestation(**attestation.model_dump())
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att

@router.get("/", response_model=List[schemas.AttestationOut])
def get_attestations(db: Session = Depends(get_db)):
    return db.query(models.Attestation).all()