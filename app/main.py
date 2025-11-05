from fastapi import FastAPI
from app.api.v1.users import router as users_router
from app.api.v1.products import router as products_router
from app.db.session import engine
from app.db.base import Base
from app.db import models 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(products_router, prefix="/api/v1/products", tags=["products"])