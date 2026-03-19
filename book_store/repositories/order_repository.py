from sqlalchemy.orm import Session
from models import Order


def create_order(db: Session, order: Order):
    db.add(order)
    # db.commit() прибрано, щоб керувати транзакцією в сервісі
    db.flush()
    db.refresh(order)
    return order


def get_all_orders(db: Session):
    return db.query(Order).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def update_order(db: Session, order_id: int, data):
    order = get_order(db, order_id)
    if not order:
        return None

    # Використовуємо dict(exclude_unset=True) якщо data - це Pydantic схема
    update_data = data.dict(exclude_unset=True) if hasattr(data, 'dict') else data

    for key, value in update_data.items():
        setattr(order, key, value)

    db.commit()
    db.refresh(order)
    return order


def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    if not order:
        return None

    db.delete(order)
    db.commit()
    return order