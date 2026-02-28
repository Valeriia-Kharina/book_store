from sqlalchemy.orm import Session
from models import ReturnBook

def create_return(db, ret):
    db.add(ret)
    db.commit()
    db.refresh(ret)
    return ret

def get_all_returns(db: Session):
    return db.query(ReturnBook).all()

def get_return(db: Session, return_id: int):
    return db.query(ReturnBook).filter(ReturnBook.id == return_id).first()

def update_return(db: Session, return_id: int, data):
    ret = get_return(db, return_id)
    if not ret:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(ret, key, value)

    db.commit()
    db.refresh(ret)
    return ret

def delete_return(db: Session, return_id: int):
    ret = get_return(db, return_id)
    if not ret:
        return None

    db.delete(ret)
    db.commit()
    return ret