#!/usr/bin/python3
"""
contains class Review
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Order(BaseModel, Base):
    """
    describes the orders table
    """
    __tablename__ = 'orders'
    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
    item_name = Column(String(256), nullable=False)
    item_price = Column(String(256), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)

