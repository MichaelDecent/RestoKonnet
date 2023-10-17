#!/usr/bin/python3
"""
contains class Restaurant 
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Restaurant(BaseModel, Base):
    """
    describes the restaurants table
    """
    __tablename__ = 'restaurants'
    vendor_id = Column(String(60), ForeignKey('vendors.id'), nullable=False)
    name = Column(String(60), nullable=False)
    address = Column(String(256), nullable=False)
    reviews = relationship("Review", backref="restaurant", cascade="all, delete, delete-orphan")
    items = relationship("Item", backref="restaurant", cascade="all, delete, delete-orphan")
