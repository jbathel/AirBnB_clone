#!/usr/bin/python3
"""
This is a Amenity Module for AirBnB
"""

class Amenity(BaseModel):
    """Amenity Model"""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""
    super().__init__(self, *args, **kwargs)

    name = ''
