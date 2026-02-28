from sqlalchemy.orm import Session
from models import Subscription


def create_subscription(db: Session, subscription: Subscription):
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription


def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()

def update_subscription(db, subscription: Subscription):
    db.commit()
    db.refresh(subscription)
    return subscription


def delete_subscription(db, subscription: Subscription):
    db.delete(subscription)
    db.commit()