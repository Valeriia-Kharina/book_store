from pydantic import BaseModel
from typing import Optional

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True