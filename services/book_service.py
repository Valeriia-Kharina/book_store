from sqlalchemy.orm import Session
from repositories import book_repository

def create_book(db: Session, book_data):
    if book_data.price < 0:
        raise ValueError("Ціна не може бути від’ємною")
    return book_repository.create_book(db, book_data)

def get_book(db: Session, book_id: int):
    return book_repository.get_book_by_id(db, book_id)

def get_books(db: Session):
    return book_repository.get_all_books(db)

def update_book(db: Session, book_id: int, book_data):
    return book_repository.update_book(db, book_id, book_data)

def delete_book(db: Session, book_id: int):
    return book_repository.delete_book(db, book_id)