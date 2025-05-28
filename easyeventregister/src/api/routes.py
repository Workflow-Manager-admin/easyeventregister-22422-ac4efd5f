# API router for events and registration.
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# PUBLIC_INTERFACE
@router.get("/events", response_model=List[models.Event])
def list_events(db: Session = Depends(get_db)):
    """List all events (both upcoming and past)."""
    return crud.get_events(db)


# PUBLIC_INTERFACE
@router.get("/events/{event_id}", response_model=models.Event)
def get_event_detail(event_id: int, db: Session = Depends(get_db)):
    """Get details for a specific event by ID."""
    db_event = crud.get_event(db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


# PUBLIC_INTERFACE
@router.post("/events/{event_id}/register", response_model=models.Registration)
def register_for_event(
    event_id: int,
    registration: models.RegistrationCreate,
    db: Session = Depends(get_db)
):
    """Register a user for a specific event."""
    event = crud.get_event(db, event_id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return crud.create_registration(db, event_id=event_id, reg=registration)
