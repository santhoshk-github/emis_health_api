# usr/bin/python
from sqlalchemy import Column, Integer, String,Date
from database import Base

### Patient table class
class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    date_of_birth = Column(String(10))
    medical_history = Column(String(250))
    lab_results = Column(String(250))
