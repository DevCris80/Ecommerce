from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int

class ProductCreate(ProductBase):
    pass    

class ProductRead(ProductBase):
    product_id: int
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)