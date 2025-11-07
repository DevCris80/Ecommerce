from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.orders import OrderCreate, OrderRead
from app.services.order_logic import OrderService

router = APIRouter()

@router.get("/", response_model = list[OrderRead])
async def read_orders(db: Session = Depends(get_db)):
    order_service = OrderService(db)
    orders = order_service.list_orders()
    return orders

@router.post("/", response_model=OrderRead)
async def create_order(order_create: OrderCreate, db: Session = Depends(get_db)):
    order_service = OrderService(db)
    order = order_service.create_order(order_create)
    return order

@router.get("/{order_id}", response_model=OrderRead)
async def read_order(order_id: int, db: Session = Depends(get_db)):
    order_service = OrderService(db)
    order = order_service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order