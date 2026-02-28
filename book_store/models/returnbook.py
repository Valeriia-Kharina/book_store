from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class ReturnBook(Base):
    __tablename__ = "returnbook"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    quantity = Column(Integer)
    return_date = Column(DateTime, default=datetime.utcnow)
    reason = Column(String)

    order = relationship("Order", back_populates="returns")
    book = relationship("Book")
