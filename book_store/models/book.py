from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    reserved_stock = Column(Integer, default=0)

    author = relationship("Author", back_populates="books")
    preorders = relationship("PreOrder", back_populates="book")
    order_item = relationship("OrderItem", back_populates="book")