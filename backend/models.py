from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String) # Will store 'patient' or 'therapist'

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(String, primary_key=True, index=True) # UUID or similar
    patient_username = Column(String, index=True)
    therapist_username = Column(String, index=True)
    date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    status = Column(String)
    type = Column(String)
