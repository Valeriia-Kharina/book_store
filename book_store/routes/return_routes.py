from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.return_schema import ReturnCreate, ReturnResponse, ReturnUpdate
from services import return_service
from database import SessionLocal

router = APIRouter(prefix="/return_book", tags=["Return Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReturnResponse)
def return_book(ret: ReturnCreate, db: Session = Depends(get_db)):
    return return_service.return_book(db, ret)

@router.get("/", response_model=list[ReturnResponse])
def get_returns(db: Session = Depends(get_db)):
    return return_service.get_returns(db)

@router.put("/{return_id}", response_model=ReturnResponse)
def update_return(return_id: int, ret: ReturnUpdate, db: Session = Depends(get_db)):
    updated = return_service.update_return(db, return_id, ret)
    if not updated:
        raise HTTPException(status_code=404, detail="Return not found")
    return updated

@router.delete("/{return_id}")
def delete_return(return_id: int, db: Session = Depends(get_db)):
    deleted = return_service.delete_return(db, return_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Return not found")
    return {"message": "Return deleted"}