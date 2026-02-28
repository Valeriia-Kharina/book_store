from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    frequency = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    type = Column(String, default="journal")

    subscriptions = relationship("Subscription", back_populates="journal")
