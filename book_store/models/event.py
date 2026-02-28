from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    event_date = Column(Text)
    event_time = Column(Text)
    location = Column(Text)

    registrations = relationship("EventRegistration", back_populates="event")

    
