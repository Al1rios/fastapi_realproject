from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.model import Product
from src.schemas import schema
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repository.product import RepositoryProduct


create_db()
app = FastAPI()

@app.post("/products")
def create_product(product: schema.Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created


@app.get("/products")
def lister_products():
    return {"message":"lister productos"}
