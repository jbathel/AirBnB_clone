#!/usr/bin/python3
"""
This is a User Module for AirBnB
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Model"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
