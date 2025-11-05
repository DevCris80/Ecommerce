from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    sku: str
    

class ProductRead(ProductBase):
    id: int
    created_at: Optional[str] = None

    class Config:
        orm_mode = True