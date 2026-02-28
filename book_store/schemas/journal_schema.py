from pydantic import BaseModel

class JournalCreate(BaseModel):
    title: str
    publisher: str
    price: float
    frequency: str
    stock: int

class JournalResponse(JournalCreate):
    id: int

    class Config:
        from_attributes = True