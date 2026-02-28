from sqlalchemy.orm import Session
from models.event import Event


def create_event(db: Session, event):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_all_events(db: Session):
    return db.query(Event).all()


def get_event_by_id(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def update_event(db, event_id: int, event_data):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        return None

    for field, value in event_data.dict(exclude_unset=True).items():
        setattr(event, field, value)

    db.commit()
    db.refresh(event)

    return event

def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
    return event