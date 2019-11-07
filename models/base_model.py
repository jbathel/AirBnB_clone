#!/usr/bin/python3
"""
This is a Base Module for AirBnB
"""
from datetime import datetime
import json, uuid


class BaseModel():
    """Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialize Public Attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        try:
            self.id
        except:
            self.id = str(uuid.uuid4())
        try:
            self.created_at
        except:
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """..."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    def save(self):
        """..."""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """..."""
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        if self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, datetime) is True:
                    value = value.isoformat()
                dictionary[key] = value
        return dictionary
