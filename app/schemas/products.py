from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass    

class ProductRead(ProductBase):
    id: int
    created_at: Optional[str] = None

    class Config:
        from_attributes = True