from sqlalchemy.orm import Session

from models import PreOrder, Book
from repositories import preorder_repository


def create_preorder(db: Session, data):

    book = db.query(Book).filter(
        Book.id == data.book_id
    ).first()

    if not book:
        raise ValueError("Книга не знайдена")


    preorder = PreOrder(

        customer_id=data.customer_id,
        book_id=data.book_id,
        status="очікується"

    )

    return preorder_repository.create_preorder(
        db,
        preorder
    )


def get_preorders(db: Session):

    return preorder_repository.get_all_preorders(db)

def update_preorder(
        db: Session,
        preorder_id: int,
        customer_id: int,
        book_id: int
):
    preorder = db.query(PreOrder).filter(
        PreOrder.id == preorder_id
    ).first()

    if not preorder:
        return None

    preorder.customer_id = customer_id
    preorder.book_id = book_id

    db.commit()
    db.refresh(preorder)

    return preorder


def delete_preorder(
        db: Session,
        preorder_id: int
):

    preorder = db.query(PreOrder).filter(
        PreOrder.id == preorder_id
    ).first()

    if not preorder:
        return None

    db.delete(preorder)
    db.commit()

    return True