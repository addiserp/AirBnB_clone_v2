#!/usr/bin/python
""" This is a class using DBStorage - Review"""
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """A representation of Review Class"""

    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """It initializes Review"""

        super().__init__(*args, **kwargs)
