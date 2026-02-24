from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.book_schema import BookCreate, BookUpdate, BookResponse
from services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не знайдена")
    return book

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return book_service.get_books(db)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    updated = book_service.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не знайдена")
    return updated

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = book_service.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не знайдена")
    return {"message": "Книга видалена"}