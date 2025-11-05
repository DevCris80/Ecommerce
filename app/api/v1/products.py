from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.products import ProductCreate, ProductRead
from app.db.models import Product
from app.services.product_logic import ProductService

router = APIRouter()

@router.get("/", response_model=list[ProductRead])
async def read_products(db: Session = Depends(get_db)):
    product_service = ProductService(db)
    products = product_service.list_products()
    return products

@router.post("/", response_model=ProductRead)
async def create_product(product_create: ProductCreate, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    product = product_service.create_product(product_create)
    return product

@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/sku/{sku}", response_model=ProductRead)
async def read_product_by_sku(sku: str, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    product = product_service.get_product_by_sku(sku)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product