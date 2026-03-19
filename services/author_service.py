from sqlalchemy.orm import Session

from repositories import author_repository


def create_author(db: Session, data):
    return author_repository.create_author(db, data)

def get_authors(db: Session):
    return author_repository.get_all_authors(db)

def get_books_by_author(db: Session, author_id: int):
    return author_repository.get_books_by_author(db, author_id)

def update_author(db, author_id, data):
    return author_repository.update_author(db, author_id, data)

def delete_author(db, author_id):
    return author_repository.delete_author(db, author_id)