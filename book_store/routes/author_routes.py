from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.author_schema import AuthorCreate, AuthorResponse, AuthorUpdate
from schemas.book_schema import BookResponse
from services import author_service
from database import SessionLocal


router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(db, author)

@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return author_service.get_authors(db)

@router.get("/{author_id}/books", response_model=list[BookResponse])
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    return author_service.get_books_by_author(db, author_id)

@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    updated = author_service.update_author(db, author_id, author)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated

@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    deleted = author_service.delete_author(db, author_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted"}