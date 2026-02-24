from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    email = Column(String)
    phone = Column(String)

    orders = relationship("Order", back_populates="customer")
    preorders = relationship("PreOrder", back_populates="customer")
    subscriptions = relationship("Subscription", back_populates="customer")
    event_registrations = relationship("EventRegistration", back_populates="customer")
