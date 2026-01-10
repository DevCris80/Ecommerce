from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.deps import get_user_service
from app.schemas.auth import TokenResponse
from app.services.auth import create_access_token
from app.services.user_logic import UserService

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(
    token_request: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.authenticate_user(
        token_request.username, token_request.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(subject=str(user.user_id))

    return TokenResponse(access_token=access_token, token_type="bearer")
