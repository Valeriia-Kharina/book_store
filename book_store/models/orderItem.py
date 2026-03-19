from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    quantity = Column(Integer)
    price = Column(Float)  # ціна за позицію

    order = relationship("Order", back_populates="items")
    book = relationship("Book", back_populates="order_item")