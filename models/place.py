#!/usr/bin/python3
"""
This is a Place Module for AirBnB
"""

class Place(BaseModel):
    """Place Model"""

    def __init__(self, *args, **kwargs):
        """Initialize Place instance"""
    super().__init__(self, *args, **kwargs)

    city_id = ''#it will be the City.id
    user_id = '' #it will be the User.id
    name: string = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] #it will be the list of Amenity.id
