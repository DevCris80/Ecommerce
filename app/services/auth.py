import jwt
from datetime import datetime, timedelta, timezone

from app.core.config import settings

ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = settings.SECRET_KEY


def create_access_token(data: dict) -> str:
    to_encode: dict = data.copy()
    now = datetime.now(timezone.utc)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt