from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass    

class ProductRead(ProductBase):
    product_id: int
    created_at: datetime = None

    class Config:
        from_attributes = True