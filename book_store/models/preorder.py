from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base

class PreOrder(Base):
    __tablename__ = "preorder"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    preorder_date = Column(DateTime, default=datetime.utcnow)
    # НОВЕ: до коли діє резерв (наприклад, +3 дні)
    reserved_until = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=3))
    # НОВЕ: чи діє резерв зараз
    is_active = Column(Boolean, default=True)
    quantity = Column(Integer, default=1)
    status = Column(String, default="очікується")  # очікується, доставлено, скасовано

    customer = relationship("Customer", back_populates="preorders")
    book = relationship("Book", back_populates="preorders")