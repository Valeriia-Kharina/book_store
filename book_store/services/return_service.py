from sqlalchemy.orm import Session

from models import ReturnBook, Book
from repositories import return_repository


def return_book(db, data):
    book = db.query(Book).filter(Book.id == data.book_id).first()

    book.stock += data.quantity

    ret = ReturnBook(**data.dict())
    return return_repository.create_return(db, ret)

def get_returns(db: Session):
    return return_repository.get_all_returns(db)

def update_return(db, return_id, data):
    return return_repository.update_return(db, return_id, data)

def delete_return(db, return_id):
    return return_repository.delete_return(db, return_id)
