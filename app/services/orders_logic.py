from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Order
from app.schemas.orders import OrderCreate


class OrderService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_orders(self):
        result = await self.db.execute(select(Order))
        return result.scalars().all()

    async def get_order_by_id(self, order_id: int) -> Order:
        result = await self.db.execute(select(Order).where(Order.order_id == order_id))
        return result.scalars().first()

    async def create_order(self, order_data: OrderCreate) -> Order:
        new_order = Order(
            total_amount=order_data.total_amount,
            status=order_data.status,
            user_id=order_data.user_id
        )
        self.db.add(new_order)
        await self.db.commit()
        await self.db.refresh(new_order)
        return new_order
    
    async def delete_order(self, order_id: int) -> None:
        order = self.get_order_by_id(order_id)
        self.db.delete(order)
        await self.db.commit()