from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    full_name: Optional[str]
    password: str
    role: str = "customer"

class UserUpdate(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]

class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str

class UserRead(BaseModel):
    user_id: int
    email: EmailStr
    full_name: Optional[str]
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes = True)