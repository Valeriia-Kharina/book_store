import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class PreOrder(Base):
    __tablename__ = "preorder"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    preorder_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # очікується, доставлено, скасовано

    customer = relationship("Customer", back_populates="preorders")
    book = relationship("Book", back_populates="preorders")
