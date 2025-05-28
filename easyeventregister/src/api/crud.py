# CRUD utility functions for events and registrations.

from sqlalchemy.orm import Session
from . import database
from .models import EventCreate, RegistrationCreate


# PUBLIC_INTERFACE
def get_event(db: Session, event_id: int):
    """Get event details by ID."""
    return db.query(database.Event).filter(database.Event.id == event_id).first()

# PUBLIC_INTERFACE


def get_events(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of events."""
    return (
        db.query(database.Event)
        .order_by(database.Event.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# PUBLIC_INTERFACE
def create_event(db: Session, event: EventCreate):
    """Create a new event."""
    db_event = database.Event(
        name=event.name,
        description=event.description,
        location=event.location,
        date=event.date,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# PUBLIC_INTERFACE
def create_registration(db: Session, event_id: int, reg: RegistrationCreate):
    """Create a registration for a specific event."""
    db_reg = database.Registration(
        event_id=event_id,
        name=reg.name,
        email=reg.email,
    )
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    return db_reg


# PUBLIC_INTERFACE
def get_registrations_for_event(db: Session, event_id: int):
    """Get all registrations for a single event."""
    return (
        db.query(database.Registration)
        .filter(database.Registration.event_id == event_id)
        .all()
    )
