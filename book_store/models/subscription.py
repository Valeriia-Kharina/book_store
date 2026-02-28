from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Subscription(Base):
    __tablename__ = "subscription"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    journal_id = Column(Integer, ForeignKey("journal.id"))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    status = Column(String, default="active")

    customer = relationship("Customer", back_populates="subscriptions")
    journal = relationship("Journal", back_populates="subscriptions")