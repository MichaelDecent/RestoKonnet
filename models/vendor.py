#!/usr/bin/python3
"""
contains class Vendor
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

class Vendor(BaseModel, Base):
    """
    describes the vendors table
    """
    __tablename__ = 'vendors'
    name = Column(String(60), nullable=False)
    phone_no = Column(String(60), nullable=False, unique=True)
    address = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False, unique=True)
    email = Column(String(60), nullable=False, unique=True)
    restaurants = relationship('Restaurant', backref="vendor", uselist=False, cascade="all, delete, delete-orphan")
    cart_items = relationship('CartItem', backref="vendor", cascade="all, delete, delete-orphan")


    def __init__(self, *args, **kwargs):
        """initializes vendor"""
        super().__init__(*args, **kwargs)
    
    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = generate_password_hash(value)
        super().__setattr__(name, value)
