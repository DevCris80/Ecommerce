from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import asyncio

from app.db.models import User
from app.schemas.users import UserCreate
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_users(self) -> list[User]:
        query = await self.db.execute(select(User))
        return query.scalars().all()

    async def get_user_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(select(User).filter(User.user_id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).filter(User.email == email))
        result = result.scalars().first()
        return result

    async def create_user(self, user_create: UserCreate) -> User:
        try:
            hashed_password = await asyncio.to_thread(get_password_hash, user_create.password)

            new_user = User(
                email=user_create.email,
                full_name=user_create.full_name,
                hashed_password=hashed_password
            )

            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)
            return new_user
        
        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered")
    
    async def authenticate_user(self, email: str, password: str) -> User | None:
        user = await self.get_user_by_email(email)

        if not user:
            return None

        is_valid = await asyncio.to_thread(verify_password, password, user.hashed_password)

        if not is_valid:
            return None
        return user
    
    async def delete_user(self, user_id: int):
        user = await self.get_user_by_id(user_id)
        await self.db.delete(user)
        await self.db.commit()