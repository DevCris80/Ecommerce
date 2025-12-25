from enum import StrEnum

class UserRole(StrEnum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    SELLER = "seller"

class OrderStatus(StrEnum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"

