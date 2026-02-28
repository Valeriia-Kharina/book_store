from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.event_schema import EventCreate, EventResponse, EventUpdate
from repositories import event_repository

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_repository.create_event(db, event)


@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return event_repository.get_all_events(db)


@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = event_repository.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Подію не знайдено")
    return event


@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    updated_event = event_repository.update_event(db, event_id, event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Подію не знайдено")
    return updated_event


@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    deleted = event_repository.delete_event(db, event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Подію не знайдено")
    return {"message": "Подію видалено"}