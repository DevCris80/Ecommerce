from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import OrderStatus


class OrderCreate(BaseModel):
    status: OrderStatus
    total_amount: float
    user_id: int


class OrderRead(BaseModel):
    order_id: int
    status: str
    total_amount: float
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
