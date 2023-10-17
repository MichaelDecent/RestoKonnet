#!/usr/bin/python3
"""
contains class Vendor
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Vendor(BaseModel, Base):
    """
    describes the vendors table
    """
    __tablename__ = 'vendors'
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    phone_no = Column(String(60), nullable=False, unique=True)
    address = Column(String(256), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    restaurants = relationship("Restaurant", backref="vendor", cascade="all, delete, delete-orphan")


