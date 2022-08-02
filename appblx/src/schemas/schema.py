from matplotlib.style import available
from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    # my_products: List[Product]
    # my_sales: List[PurchaseOrder]
    # my_purcharse_order: List[PurchaseOrder]

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True

class PurchaseOrder(BaseModel):
    id: Optional[str] = None
    # user: User
    # product: Product
    amount: int
    delivery: bool = True
    address: str
    comment: Optional[str] = "no comment"





