from sqlalchemy import ForeignKey, func, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from enum import StrEnum

from app.db.base import Base

class OrderStatus(StrEnum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column(default="customer", nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] =  mapped_column(primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    stock_quantity: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    order_items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    
    order_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    total_amount: Mapped[float] = mapped_column(nullable=False, default=0.0)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="orders", foreign_keys=[user_id])

    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    __table_args__ = (UniqueConstraint("order_id", "product_id", name="uq_order_product"),)

    order_item_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    quantity: Mapped[int] = mapped_column(nullable=False)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="order_items")