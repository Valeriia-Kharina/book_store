from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from services.journal_service import JournalService
from schemas.journal_schema import JournalCreate, JournalResponse

router = APIRouter(prefix="/journals", tags=["Journals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=JournalResponse)
def create_journal(journal: JournalCreate, db: Session = Depends(get_db)):
    service = JournalService(db)
    return service.create_journal(journal)

@router.get("/", response_model=list[JournalResponse])
def get_all(db: Session = Depends(get_db)):
    service = JournalService(db)
    return service.get_all()

@router.put("/{journal_id}", response_model=JournalResponse)
def update_journal(
        journal_id: int,
        journal: JournalCreate,
        db: Session = Depends(get_db)
):
    service = JournalService(db)
    updated_journal = service.update(journal_id, journal)

    if not updated_journal:
        raise HTTPException(
            status_code=404,
            detail="Journal not found"
        )

    return updated_journal

@router.delete("/{journal_id}")
def delete_journal(
        journal_id: int,
        db: Session = Depends(get_db)
):
    service = JournalService(db)
    deleted = service.delete(journal_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Journal not found"
        )

    return {"message": "Journal deleted successfully"}