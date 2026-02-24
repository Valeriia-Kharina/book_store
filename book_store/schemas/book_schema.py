from pydantic import BaseModel
from typing import Optional

# Для створення
class BookCreate(BaseModel):
    title: str
    author_id: int
    price: float
    stock: int

# Для оновлення
class BookUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

# Для відповіді
class BookResponse(BaseModel):
    id: int
    title: str
    author_id: int
    price: float
    stock: int

    class Config:
        from_attributes = True