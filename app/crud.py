from sqlalchemy.orm import Session
from . import models, schemas

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, patient: schemas.PatientCreate):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
        return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return {"message": "Patient deleted successfully"}
    return {"message": "Patient not found"}

