from sqlalchemy.orm import Session
from models import Customer

def create_customer(db, data):
    customer = Customer(**data.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_all_customers(db: Session):
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, data):
    customer = get_customer(db, customer_id)
    if not customer:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    if not customer:
        return None

    db.delete(customer)
    db.commit()
    return customer

class CustomerRepository:
    pass