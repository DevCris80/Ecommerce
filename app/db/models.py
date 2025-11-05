from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    full_name: str = Column(String, nullable=True)
    role: str = Column(String, default="customer", nullable=False)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())

    orders = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True, index=True)
    sku: str = Column(String, unique=True, nullable=False, index=True)
    name: str = Column(String, index=True, nullable=False)
    description: str = Column(String, nullable=True)
    price: float = Column(Float, nullable=False)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())

    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    
    id: int = Column(Integer, primary_key=True, index=True)
    total_amount: float = Column(Float, nullable=False, default=0.0)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
    
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="orders", foreign_keys=[user_id])
    
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id: int = Column(Integer, primary_key=True, index=True)
    
    order_id: int = Column(Integer, ForeignKey("orders.id"), nullable=False)
    
    product_id: int = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity: int = Column(Integer, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")