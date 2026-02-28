from pydantic import BaseModel
from typing import Optional

class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    country: str

class AuthorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    country: Optional[str] = None

class AuthorResponse(AuthorCreate):
    id: int

    class Config:
        from_attributes = True