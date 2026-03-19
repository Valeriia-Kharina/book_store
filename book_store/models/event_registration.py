from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class EventRegistration(Base):
    __tablename__ = "event_registration"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("event.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    registration_date = Column(DateTime)

    event = relationship("Event", back_populates="registrations")
    customer = relationship("Customer", back_populates="event_registrations")