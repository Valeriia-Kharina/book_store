from pydantic import BaseModel
from typing import Optional

class ReturnCreate(BaseModel):
    order_id: int
    book_id: int
    quantity: int
    reason: str

class ReturnUpdate(BaseModel):
    quantity: Optional[int] = None
    reason: Optional[str] = None

class ReturnResponse(ReturnCreate):
    id: int

    class Config:
        from_attributes = True