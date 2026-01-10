from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    sku: str
    name: str
    description: str | None
    price: float
    stock_quantity: int


class ProductRead(BaseModel):
    product_id: int
    sku: str
    name: str
    description: str | None
    price: float
    stock_quantity: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
