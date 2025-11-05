from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.products import ProductCreate
from app.db.models import Product

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_create: ProductCreate) -> Product:
        if self.db.query(Product).filter(Product.sku == product_create.sku).first():
            raise HTTPException(status_code=400, detail="SKU must be unique")

        # Create and save the product model_dump is used to convert Pydantic model to dict
        product = Product(**product_create.model_dump())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def get_product_by_id(self, product_id: int) -> Product | None:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail="Product not found")
        return product

    def get_product_by_sku(self, sku: str) -> Product | None:
        return self.db.query(Product).filter(Product.sku == sku).first()
    
    def list_products(self) -> list[Product]:
        return self.db.query(Product).all()