from typing import Optional
from pydantic import BaseModel, EmailStr

class ProductBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class ProductCreate(ProductBase):
    password: str
    role: str = "customer"
    

class ProductRead(ProductBase):
    id: int
    created_at: Optional[str] = None

    class Config:
        orm_mode = True