#!/usr/bin/python3
"""
This is a City Module for AirBnB
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Model"""

    state_id = ''  # it will be the State.id
    name = ''
