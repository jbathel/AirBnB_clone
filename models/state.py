#!/usr/bin/python3
"""
This is a State Module for AirBnB
"""

class State(BaseModel):
    """State Model"""

    def __init__(self, *args, **kwargs):
        """Initialize state instance"""
        super().__init__(self, *args, **kwargs)

    name = ''
