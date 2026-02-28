from pydantic import BaseModel
from datetime import datetime


class PreOrderCreate(BaseModel):

    customer_id: int
    book_id: int


class PreOrderResponse(BaseModel):

    id: int
    customer_id: int
    book_id: int
    preorder_date: datetime
    status: str

    class Config:

        from_attributes = True