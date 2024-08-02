# usr/bin/python
from pydantic import BaseModel

### Base class
class PatientBase(BaseModel):
    name: str
    age: int
    date_of_birth: str
    medical_history: str
    lab_results: str

### Create class
class PatientCreate(PatientBase):
    pass

### orm class
class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
