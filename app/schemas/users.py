from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str
    role: str = "customer"
    

class UserRead(UserBase):
    user_id: int
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)