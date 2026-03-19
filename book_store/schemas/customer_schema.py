from pydantic import BaseModel
from typing import Optional
from enum import Enum

#лр3
class LoyaltyTier(str, Enum):
    Bronze = "Bronze"
    Silver = "Silver"
    Gold = "Gold"

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    phone: str
    loyalty_tier: LoyaltyTier = LoyaltyTier.Bronze        #лр3

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    loyalty_tier: Optional[LoyaltyTier] = None      #лр3

class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True

