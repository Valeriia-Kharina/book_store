from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.subscription_schema import SubscriptionCreate, SubscriptionResponse
from services import subscription_service
from database import SessionLocal

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SubscriptionResponse)
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    return subscription_service.create_subscription(db, subscription)


@router.get("/", response_model=list[SubscriptionResponse])
def get_subscriptions(db: Session = Depends(get_db)):
    return subscription_service.get_subscriptions(db)

@router.put("/{subscription_id}", response_model=SubscriptionResponse)
def update_subscription(subscription_id: int,
                        subscription: SubscriptionCreate,
                        db: Session = Depends(get_db)):

    updated = subscription_service.update_subscription(
        db,
        subscription_id,
        subscription
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Subscription not found")

    return updated


@router.delete("/{subscription_id}")
def delete_subscription(subscription_id: int,
                        db: Session = Depends(get_db)):

    deleted = subscription_service.delete_subscription(
        db,
        subscription_id
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Subscription not found")

    return {"message": "Subscription deleted successfully"}