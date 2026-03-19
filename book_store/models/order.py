from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

# Логіка переходів статусів (можна використовувати для валідації в сервісах)
ORDER_STATUS = {
    "Pending": ["Confirmed", "Cancelled"],
    "Confirmed": ["Shipped", "Cancelled"],
    "Shipped": ["Delivered"],
    "Delivered": [],
    "Cancelled": []
}


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))  # Переконайся, що назва таблиці 'customers'
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Pending")
    total_price = Column(Float)

    # НОВЕ: Поле для збереження застосованих промо-акцій (для прозорості звіту)
    # Зберігатимемо як рядок, розділений комами, наприклад: "Loyalty (Gold), Весняний розпродаж"
    applied_promos = Column(String, nullable=True)

    # Зв'язки
    customer = relationship("Customer", back_populates="orders")

    # Зв'язок з елементами замовлення (обов'язково для OrderItem)
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    # Зв'язок з поверненнями
    returns = relationship("ReturnBook", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    book_id = Column(Integer, ForeignKey("book.id"))  # Переконайся, що таблиця 'books'
    quantity = Column(Integer)
    price = Column(Float)  # Ціна на момент покупки

    order = relationship("Order", back_populates="items")
    book = relationship("Book", back_populates="order_item")