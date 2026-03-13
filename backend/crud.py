from sqlalchemy.orm import Session
import models, schemas
import uuid

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    # In a real app, hash the password here before saving
    db_user = models.User(username=user.username, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_therapists(db: Session):
    return db.query(models.User).filter(models.User.role == "therapist").all()

def create_appointment(db: Session, appt: schemas.AppointmentCreate):
    db_appt = models.Appointment(
        id=str(uuid.uuid4()),
        **appt.model_dump()
    )
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def get_appointments_by_username(db: Session, username: str, role: str):
    if role == "therapist":
        return db.query(models.Appointment).filter(models.Appointment.therapist_username == username).all()
    else:
        return db.query(models.Appointment).filter(models.Appointment.patient_username == username).all()
