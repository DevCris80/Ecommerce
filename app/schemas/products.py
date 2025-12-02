from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductCreate(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int

class ProductRead(BaseModel):
    product_id: int
    sku: str
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)