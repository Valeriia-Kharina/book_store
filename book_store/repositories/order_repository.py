from sqlalchemy.orm import Session
from models import Order

def create_order(db, order):
    db.add(order)
    db.commit()
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

    for key, value in data.dict(exclude_unset=True).items():
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