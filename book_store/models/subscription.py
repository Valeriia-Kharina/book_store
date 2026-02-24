from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    journal_id = Column(Integer, ForeignKey("journal.id"))
    start_date = Column(String)
    end_date = Column(String)
    status = Column(String)  # активна, завершена, скасована

    customer = relationship("Customer", back_populates="subscription")
    journal = relationship("Journal", back_populates="subscription")
