from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import User
from app.schemas.users import UserCreate
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def list_users(self) -> list[User]:
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int) -> User | None:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        return user
    
    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_create: UserCreate) -> User:
        if self.db.query(User).filter(User.email == user_create.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = get_password_hash(user_create.password)
        db_user = User(
            email=user_create.email,
            hashed_password=hashed_password,
            full_name=user_create.full_name,
            role=user_create.role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user