#!/usr/bin/python3
"""
This is a City Module for AirBnB
"""

class City(BaseModel):
    """City Model"""

    def __init__(self, *args, **kwargs):
        """Initialize city instance"""
        super().__init__(self, *args, **kwargs)

    state_id = '' #it will be the State.id
    name = ''
