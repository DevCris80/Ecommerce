from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.user_logic import UserService
from app.services.product_logic import ProductService
from app.services.orders_logic import OrderService
from app.services.order_items_logic import OrderItemService
from app.db.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    service = get_user_service(db)
    return await service.get_current_user(token)

async def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)

async def get_product_service(db: AsyncSession = Depends(get_db)) -> ProductService:
    return ProductService(db)

async def get_order_service(db: AsyncSession = Depends(get_db)) -> OrderService:
    return OrderService(db)

async def get_order_item_service(db: AsyncSession = Depends(get_db)) -> OrderItemService:
    return OrderItemService(db)