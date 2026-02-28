from pydantic import BaseModel
from datetime import datetime


class SubscriptionCreate(BaseModel):
    customer_id: int
    journal_id: int
    months: int  # для обчислення end_date


class SubscriptionResponse(BaseModel):
    id: int
    customer_id: int
    journal_id: int
    start_date: datetime
    end_date: datetime
    status: str

    class Config:
        from_attributes = True