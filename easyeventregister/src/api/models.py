# Models for EasyEventRegister: Event and Registration definitions.
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# PUBLIC_INTERFACE
class EventBase(BaseModel):
    """Base fields for an event."""
    name: str
    description: Optional[str] = None
    location: Optional[str] = None
    date: datetime

# PUBLIC_INTERFACE
class EventCreate(EventBase):
    """Fields required to create an event."""
    pass

# PUBLIC_INTERFACE
class Event(EventBase):
    """Return type fields for an event with ID."""
    id: int

    class Config:
        orm_mode = True

# PUBLIC_INTERFACE
class RegistrationBase(BaseModel):
    """Base fields for registration."""
    name: str
    email: str

# PUBLIC_INTERFACE
class RegistrationCreate(RegistrationBase):
    """Fields required for creating registration."""
    pass

# PUBLIC_INTERFACE
class Registration(RegistrationBase):
    """Return type fields for registration with ID."""
    id: int
    event_id: int

    class Config:
        orm_mode = True
