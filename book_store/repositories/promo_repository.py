from sqlalchemy.orm import Session
from models.promo import Promo
from datetime import datetime


def get_active_promos(db: Session):
    """Отримує список акцій, які діють прямо зараз за часом"""
    now = datetime.now()
    return db.query(Promo).filter(
        Promo.active_from <= now,
        Promo.active_to >= now
    ).all()


def create_promo(db: Session, promo_data: Promo):
    """Зберігає нову промо-акцію в базу даних"""
    db.add(promo_data)
    db.commit()
    db.refresh(promo_data)
    return promo_data


def get_all_promos(db: Session):
    """Повертає всі створені промо-акції для перевірки у Swagger"""
    return db.query(Promo).all()


def update_promo(db: Session, promo_id: int, data: dict):
    """Оновлює дані промо-акції"""
    promo = db.query(Promo).filter(Promo.id == promo_id).first()
    if not promo:
        return None

    for key, value in data.items():
        setattr(promo, key, value)

    db.commit()
    db.refresh(promo)
    return promo


def delete_promo(db: Session, promo_id: int):
    """Видаляє промо-акцію за її ID"""
    promo = db.query(Promo).filter(Promo.id == promo_id).first()
    if promo:
        db.delete(promo)
        db.commit()
        return True
    return False