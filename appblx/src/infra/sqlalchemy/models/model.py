from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Product(Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)