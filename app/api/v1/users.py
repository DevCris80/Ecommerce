from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.models import User
from app.schemas.users import UserCreate, UserRead
from app.db.session import get_db
from app.services.user_logic import UserService

router = APIRouter()

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user_by_id(user_id)

    
@router.get("/", response_model= list[UserRead])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)

    user_db = user_service.create_user(user)
    return user_db
