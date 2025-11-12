from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.schemas.orders import OrderRead
from app.schemas.products import ProductRead

class OrderItemBase(BaseModel):
    quantity: int

    order_id: int
    product_id: int

class OrderItemCreate(OrderItemBase):
    pass


class OrderItemRead(OrderItemBase):
    order_item_id: int
    
    model_config = ConfigDict(from_attributes = True)

class OrderItemReadWithRelations(OrderItemRead):
    order: OrderRead
    product: ProductRead