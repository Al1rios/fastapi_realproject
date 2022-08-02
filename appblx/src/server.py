from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from appblx.src.infra.sqlalchemy.models.models import Product
from src.schemas.schema import Product
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repository.product import RepositoryProduct


create_db()
app = FastAPI()

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created


@app.get("/products")
def lister_products():
    return {"message":"lister productos"}
