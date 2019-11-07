#!/usr/bin/python3
"""
This is a Review Module for AirBnB
"""

class Review(BaseModel):
    """Review Model"""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance"""
        super().__init__(self, *args, **kwargs)

    place_id = '' #it will be the Place.id
    user_id = '' #it will be the User.id
    text = ''
