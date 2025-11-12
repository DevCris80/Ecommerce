from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    total_amount: float
    user_id: int

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: datetime = None

    class Config:
        from_attributes = True