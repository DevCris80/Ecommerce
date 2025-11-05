from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str
    role: str = "customer"
    

class UserRead(UserBase):
    id: int
    created_at: Optional[str] = None

    class Config:
        from_attributes = True