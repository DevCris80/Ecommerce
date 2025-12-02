from fastapi import FastAPI
from app.api.v1.users import router as users_router
from app.api.v1.products import router as products_router
from app.api.v1.orders import router as orders_router

app = FastAPI()

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(products_router, prefix="/api/v1/products", tags=["products"])
app.include_router(orders_router, prefix="/api/v1/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Welcome to the DevCris80's E-commerce API"}