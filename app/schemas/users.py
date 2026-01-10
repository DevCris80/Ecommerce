from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas.enums import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str | None
    password: str
    role: UserRole = UserRole.CUSTOMER


class UserUpdate(BaseModel):
    full_name: str | None
    email: EmailStr | None


class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str


class UserRead(BaseModel):
    user_id: int
    email: EmailStr
    full_name: str | None
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
