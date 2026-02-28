from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    customer_id: int
    book_id: int
    quantity: int

class OrderUpdate(BaseModel):
    quantity: Optional[int] = None
    status: Optional[str] = None

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    book_id: int
    quantity: int
    total_price: float

    class Config:
        from_attributes = True