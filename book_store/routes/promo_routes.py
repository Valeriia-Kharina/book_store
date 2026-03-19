from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.promo_schema import PromoCreate, PromoResponse
from models.promo import Promo
from repositories import promo_repository

router = APIRouter(prefix="/promos", tags=["Promotions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PromoResponse)
def create_new_promo(promo: PromoCreate, db: Session = Depends(get_db)):
    db_promo = Promo(**promo.dict())
    return promo_repository.create_promo(db, db_promo)

@router.get("/", response_model=list[PromoResponse])
def list_promos(db: Session = Depends(get_db)):
    return promo_repository.get_all_promos(db)

# НОВЕ: Оновлення промо
@router.put("/{promo_id}", response_model=PromoResponse)
def update_promo(promo_id: int, promo: PromoCreate, db: Session = Depends(get_db)):
    updated_promo = promo_repository.update_promo(db, promo_id, promo.dict())
    if not updated_promo:
        raise HTTPException(status_code=404, detail="Promo not found")
    return updated_promo

# НОВЕ: Видалення промо
@router.delete("/{promo_id}")
def delete_promo(promo_id: int, db: Session = Depends(get_db)):
    success = promo_repository.delete_promo(db, promo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Promo not found")
    return {"message": "Promo deleted successfully"}