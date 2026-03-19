from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import Subscription, Journal
from repositories import subscription_repository


def create_subscription(db: Session, data):
    journal = db.query(Journal).filter(Journal.id == data.journal_id).first()
    if not journal:
        raise ValueError("Журнал не знайдено")

    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=30*data.months)

    subscription = Subscription(
        customer_id=data.customer_id,
        journal_id=data.journal_id,
        start_date=start_date,
        end_date=end_date,
        status="active"
    )

    return subscription_repository.create_subscription(db, subscription)


def get_subscriptions(db: Session):
    return subscription_repository.get_all_subscriptions(db)

def update_subscription(db: Session, subscription_id: int, data):

    subscription = db.query(Subscription).filter(
        Subscription.id == subscription_id
    ).first()

    if not subscription:
        return None

    journal = db.query(Journal).filter(
        Journal.id == data.journal_id
    ).first()

    if not journal:
        raise ValueError("Журнал не знайдено")

    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=30 * data.months)

    subscription.customer_id = data.customer_id
    subscription.journal_id = data.journal_id
    subscription.start_date = start_date
    subscription.end_date = end_date
    subscription.status = "active"

    return subscription_repository.update_subscription(db, subscription)

def delete_subscription(db: Session, subscription_id: int):

    subscription = db.query(Subscription).filter(
        Subscription.id == subscription_id
    ).first()

    if not subscription:
        return None

    subscription_repository.delete_subscription(db, subscription)
    return True