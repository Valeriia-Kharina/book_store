from sqlalchemy.orm import Session
from models.book import Book

def create_book(db: Session, book_data):
    book = Book(**book_data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_all_books(db: Session):
    return db.query(Book).all()

def update_book(db: Session, book_id: int, book_data):
    book = get_book_by_id(db, book_id)
    if not book:
        return None

    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        return None

    db.delete(book)
    db.commit()
    return book