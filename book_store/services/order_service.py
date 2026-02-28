from sqlalchemy.orm import Session

from models import Book, Order
from repositories import order_repository


def create_order(db: Session, data):
    book = db.query(Book).filter(Book.id == data.book_id).first()

    if not book:
        raise ValueError("Книга не знайдена")

    if book.stock < data.quantity:
        raise ValueError("Недостатньо на складі")

    total_price = book.price * data.quantity

    book.stock -= data.quantity

    order = Order(
        customer_id=data.customer_id,
        book_id=data.book_id,
        quantity=data.quantity,
        total_price=total_price,
        status="completed"
    )

    return order_repository.create_order(db, order)

def get_orders(db: Session):
    return order_repository.get_all_orders(db)

def update_order(db, order_id, data):
    return order_repository.update_order(db, order_id, data)

def delete_order(db, order_id):
    return order_repository.delete_order(db, order_id)