from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrderCreate(BaseModel):
    status: str
    total_amount: float
    user_id: int

class OrderRead(BaseModel):
    order_id: int
    status: str
    total_amount: float
    user_id: int
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)