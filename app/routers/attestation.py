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

@router.get("/{attestation_id}", response_model=schemas.AttestationOut)
def get_attestation(attestation_id: int, db: Session = Depends(get_db)):
    att = db.query(models.Attestation).filter(models.Attestation.id == attestation_id).first()
    if not att:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return att

@router.put("/{attestation_id}", response_model=schemas.AttestationOut)
def update_attestation(attestation_id: int, attestation: schemas.AttestationCreate, db: Session = Depends(get_db)):
    db_att = db.query(models.Attestation).filter(models.Attestation.id == attestation_id).first()
    if not db_att:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    for key, value in attestation.model_dump(exclude_unset=True).items():
        setattr(db_att, key, value)
    db.commit()
    db.refresh(db_att)
    return db_att

@router.delete("/{attestation_id}")
def delete_attestation(attestation_id: int, db: Session = Depends(get_db)):
    db_att = db.query(models.Attestation).filter(models.Attestation.id == attestation_id).first()
    if not db_att:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    db.delete(db_att)
    db.commit()
    return {"message": "Запись удалена"}