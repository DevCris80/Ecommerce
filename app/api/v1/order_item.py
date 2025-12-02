from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.deps import get_order_item_service
from app.services.order_items_logic import OrderItemService
from app.schemas.order_items import OrderItemCreate, OrderItemRead

router = APIRouter()

@router.get("/{order_item_id}", response_model=OrderItemRead)
async def read_order_item(order_item_id: int, order_item_service: OrderItemService = Depends(get_order_item_service)):
    order_item = await order_item_service.get_order_item_by_id(order_item_id)
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return order_item