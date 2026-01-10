from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from app.core.config import settings

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
SECRET_KEY = settings.SECRET_KEY


def create_access_token(
    subject: str | Any, expires_delta: timedelta | None = None
) -> str:
    to_encode = {"sub": str(subject)}
    now = datetime.now(timezone.utc)

    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire, "iat": now})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
