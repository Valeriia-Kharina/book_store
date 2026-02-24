from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher = Column(String)
    price = Column(Float)
    frequency = Column(String)
    stock = Column(Integer)
    type = Column(String)

    subscriptions = relationship("Subscription", back_populates="journal")

