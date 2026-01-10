from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.deps import get_order_service
from app.schemas.orders import OrderCreate, OrderRead
from app.services.orders_logic import OrderService

router = APIRouter()


@router.get("/", response_model=list[OrderRead])
async def read_orders(order_service: OrderService = Depends(get_order_service)):
    orders = await order_service.list_orders()
    return orders


@router.post("/", response_model=OrderRead)
async def create_order(
    order_create: OrderCreate, order_service: OrderService = Depends(get_order_service)
):
    order = await order_service.create_order(order_create)
    return order


@router.get("/{order_id}", response_model=OrderRead)
async def read_order(
    order_id: int, order_service: OrderService = Depends(get_order_service)
):
    order = await order_service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
