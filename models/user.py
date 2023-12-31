#!/usr/bin/python
""" This is a class using DBStorage - User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ A representation of a user
    User inherits from BaseModel and Base.
    """

    if models.storage_t == 'db':
        __tablename__ = 'users'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        
        reviews = relationship("Review", backref="user")

    else:
        first_name = ""
        last_name = ""
        email = ""
        password = ""

    def __init__(self, *args, **kwargs):
        """It initializes user class"""

        super().__init__(*args, **kwargs)
