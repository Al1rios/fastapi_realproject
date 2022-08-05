from sqlalchemy.orm import Session
from src.schemas.schema import Product 
from src.infra.sqlalchemy.models.model import Product 

class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product):
        db_product = Product(
            name = product.name,
            details = product.details,
            price = product.price,
            available = product.available
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def lister(self):
        products = self.db.query(model.Product).all()
        return products

    def get_product(self):
        pass

    def delete(self):
        pass

        
        