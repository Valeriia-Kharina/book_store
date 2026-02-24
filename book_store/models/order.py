import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # нове, обробляється, виконано
    total_price = Column(Float)

    customer = relationship("Customer", back_populates="order")
    book = relationship("Book", back_populates="order")
    returns = relationship("ReturnBook", back_populates="order")
