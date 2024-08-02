# usr/bin/python
from sqlalchemy.orm import Session
import models, schemas

### retrieve patient detail
def get_patient(db: Session, patient_id: int):
    print("message: Patient detail display")
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

### create patient
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    print("message: Patient created successfully")
    return db_patient

### update patient
def update_patient(db: Session, patient_id: int, patient: schemas.PatientCreate):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
        print("message: Patient updated successfully")
        return db_patient

### delete patient
def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return {"message": "Patient deleted successfully"}
    return {"message": "Patient not found"}

