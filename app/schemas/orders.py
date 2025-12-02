from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrderBase(BaseModel):
    status: str
    total_amount: float
    user_id: int

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    order_id: int
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)