from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    role: str = "customer"

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str

class UserRead(BaseModel):
    user_id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: str
    created_at: datetime = None

    model_config = ConfigDict(from_attributes = True)