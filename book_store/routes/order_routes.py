from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.order_schema import OrderCreate, OrderResponse, OrderUpdate
from services import order_service
from database import SessionLocal

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        return order_service.create_order(db, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return order_service.get_orders(db)

@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    updated = order_service.update_order(db, order_id, order)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted = order_service.delete_order(db, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted"}

@router.patch("/{order_id}/status")
def update_status(order_id: int, status: str, db: Session = Depends(get_db)):
    """Метод для зміни статусу (наприклад, Cancelled для звільнення резерву)"""
    updated = order_service.update_order_status(db, order_id, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated