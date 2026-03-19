from sqlalchemy.orm import Session

from repositories import customer_repositories


def create_customer(db: Session, data):
    return customer_repositories.create_customer(db, data)

def get_customers(db: Session):
    return customer_repositories.get_all_customers(db)

def update_customer(db, customer_id, data):
    return customer_repositories.update_customer(db, customer_id, data)

def delete_customer(db, customer_id):
    return customer_repositories.delete_customer(db, customer_id)