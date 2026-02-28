from sqlalchemy.orm import Session
from models import Author
from models.book import Book

def create_author(db, data):
    author = Author(**data.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_all_authors(db: Session):
    return db.query(Author).all()

def get_books_by_author(db: Session, author_id: int):
    return db.query(Book).filter(Book.author_id == author_id).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def update_author(db: Session, author_id: int, data):
    author = get_author(db, author_id)
    if not author:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(author, key, value)

    db.commit()
    db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = get_author(db, author_id)
    if not author:
        return None

    db.delete(author)
    db.commit()
    return author