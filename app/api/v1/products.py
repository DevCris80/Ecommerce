from fastapi import APIRouter, Depends, HTTPException

from app.schemas.products import ProductCreate, ProductRead
from app.services.product_logic import ProductService
from app.api.v1.deps import get_product_service


router = APIRouter()

@router.get("/", response_model=list[ProductRead])
async def read_products(product_service: ProductService = Depends(get_product_service)):
    products = await product_service.list_products()
    return products

@router.post("/", response_model=ProductRead)
async def create_product(product_create: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    product = await product_service.create_product(product_create)
    return product

@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    product = await product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/sku/{sku}", response_model=ProductRead)
async def read_product_by_sku(sku: str, product_service: ProductService = Depends(get_product_service)):
    product = await product_service.get_product_by_sku(sku)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product