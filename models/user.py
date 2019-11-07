#!/usr/bin/python3
"""
This is a User Module for AirBnB
"""

class User(BaseModel):
    """User Model"""

    def __init__(self, *args, **kwargs):
        """Initialize user instance"""
        super().__init__(self, *args, **kwargs)

    email = ''
    password = ''
    first_name = ''
    last_name = ''
