from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.preorder_schema import (
    PreOrderCreate,
    PreOrderResponse
)

from services import preorder_service
from database import SessionLocal


router = APIRouter(
    prefix="/preorders",
    tags=["PreOrders"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/",
    response_model=PreOrderResponse
)
def create_preorder(
        preorder: PreOrderCreate,
        db: Session = Depends(get_db)
):

    return preorder_service.create_preorder(
        db,
        preorder
    )


@router.get(
    "/",
    response_model=list[PreOrderResponse]
)
def get_preorders(
        db: Session = Depends(get_db)
):

    return preorder_service.get_preorders(db)

def update_preorder(
        preorder_id: int,
        preorder: PreOrderCreate,
        db: Session = Depends(get_db)
):

    updated_preorder = preorder_service.update_preorder(
        db,
        preorder_id,
        preorder.customer_id,
        preorder.book_id
    )

    if not updated_preorder:
        raise HTTPException(
            status_code=404,
            detail="PreOrder not found"
        )

    return updated_preorder

@router.delete(
    "/{preorder_id}"
)

@router.put(
    "/{preorder_id}",
    response_model=PreOrderResponse
)
def update_preorder(
        preorder_id: int,
        preorder: PreOrderCreate,
        db: Session = Depends(get_db)
):

    updated_preorder = preorder_service.update_preorder(
        db,
        preorder_id,
        preorder.customer_id,
        preorder.book_id
    )

    if not updated_preorder:
        raise HTTPException(
            status_code=404,
            detail="PreOrder not found"
        )

    return updated_preorder

def delete_preorder(
        preorder_id: int,
        db: Session = Depends(get_db)
):

    deleted = preorder_service.delete_preorder(
        db,
        preorder_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="PreOrder not found"
        )

    return {"message": "PreOrder deleted successfully"}