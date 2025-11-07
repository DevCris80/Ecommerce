from typing import Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    total_amount: float
    user_id: int

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: Optional[str] = None

    class Config:
        from_attributes = True