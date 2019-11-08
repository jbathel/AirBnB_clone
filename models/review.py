#!/usr/bin/python3
"""
This is a Review Module for AirBnB
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Model"""

    place_id = ''  # it will be the Place.id
    user_id = ''  # it will be the User.id
    text = ''
