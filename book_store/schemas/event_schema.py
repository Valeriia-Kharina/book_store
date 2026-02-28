from pydantic import BaseModel
from typing import Optional


class EventCreate(BaseModel):
    name: str
    description: str
    event_date: str
    event_time: str
    location: str

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[str] = None
    event_time: Optional[str] = None
    location: Optional[str] = None

class EventResponse(EventCreate):
    id: int

    class Config:
        orm_mode = True