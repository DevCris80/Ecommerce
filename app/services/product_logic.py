from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.schemas.products import ProductCreate
from app.db.models import Product

class ProductService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(self, product_create: ProductCreate) -> Product:
        try:
            new_product = Product(**product_create.model_dump())
            self.db.add(new_product)
            await self.db.commit()
            await self.db.refresh(new_product)
            return new_product
        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(status_code=400, detail="Product with this SKU already exists")
    
    async def get_product_by_id(self, product_id: int) -> Product | None:
        product = await self.db.execute(select(Product).where(Product.id == product_id))
        product = product.scalars().first()
        if not product:
            raise HTTPException(status_code=400, detail="Product not found")
        return product

    async def get_product_by_sku(self, sku: str) -> Product | None:
        product = await self.db.execute(select(Product).where(Product.sku == sku))
        product = product.scalars().first()
        if not product:
            raise HTTPException(status_code=400, detail="Product not found")
        return product
    
    async def list_products(self) -> list[Product]:
        result = await self.db.execute(select(Product))
        return result.scalars().all()