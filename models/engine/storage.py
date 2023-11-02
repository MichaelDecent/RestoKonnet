#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.customer import Customer
from models.item import Item
from models.restaurant import Restaurant
from models.review import Review
from models.vendor import Vendor
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import cloudinary
from cloudinary.uploader import upload


classes = {"Customer": Customer, "Item": Item, "Restaurant": Restaurant, "Review": Review, "Vendor": Vendor}

class DBStorage:
    """ This class interacts with the MYSQL database """
    __engine = None
    __session = None
    
    def __init__(self):
        """Instantiate a DBStorage object"""
        RESTO_MYSQL_USER = getenv('RESTO_MYSQL_USER', 'root')
        RESTO_MYSQL_PWD = getenv('RESTO_MYSQL_PWD', 'root')
        RESTO_MYSQL_HOST = getenv('RESTO_MYSQL_HOST', 'localhost')
        RESTO_MYSQL_DB = getenv('RESTO_MYSQL_DB', 'restokonnect_db')
        self.__engine = create_engine('postgres://gtpfaitpogkicu:6b3bc09e6de0de49f7e2d41c039028ec754066f4c13eade81e64a5eaf348a457@ec2-3-230-24-12.compute-1.amazonaws.com:5432/dae6ljt7sfejr2')
        
        CLOUDINARY_CLOUD_NAME = "dt7ye9bd7"
        CLOUDINARY_API_KEY = "129194638594757"
        CLOUDINARY_API_SECRET = "RInU3arzIDm4IpANg0P1PS_z5bw"

        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_API_SECRET
        )
    
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class
        and its ID, or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        obj = next((value for value in
                    all_cls.values() if value.id == id), None)
        return obj

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class
        If no class is passed, returns the count of all objects in storage
        """
        if not cls:
            return len(models.storage.all())
        else:
            return len(models.storage.all(cls))
