#!/usr/bin/python3
"""
contains class Customer
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """
    name, str, customer's name
    phone_no, str, customer's phone_no
    address, str, customer's address
    email, str, customer's email
    """
    __tablename__ = 'customers'
    name = Column(String(60), nullable=False)
    phone_no = Column(String(60), nullable=False, unique=True)
    address = Column(String(256), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    reviews = relationship("Review", backref="customer", cascade="all, delete, delete-orphan")
    cart_items = relationship("CartItem", backref="customer", cascade="all, delete, delete-orphan")




    def __init__(self, *args, **kwargs):
        """initializes customer"""
        super().__init__(*args, **kwargs)
