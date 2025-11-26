from fastapi import APIRouter, Depends

from app.schemas.users import UserCreate, UserRead
from app.services.user_logic import UserService
from app.api.v1.deps import get_user_service

router = APIRouter()

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_user_by_id(user_id)

    
@router.get("/", response_model= list[UserRead])
async def read_users(user_service: UserService = Depends(get_user_service)):
    users = await user_service.list_users()
    return users


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    user_db = await user_service.create_user(user)
    return user_db

@router.delete("/{user_id}")
async def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    await user_service.delete_user(user_id)
    return {"detail": f"User {user_id} deleted successfully"}