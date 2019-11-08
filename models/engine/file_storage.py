#!/usr/bin/python3
"""
This is a module for File Storage
"""
import json


class FileStorage():
    """File Storage Model"""

    __file_path = '' #path to JSON file
    __objects = {} #<class name>.id

    @property
    def __file_path(self):
        """Getter for file path"""
        return __file_path

    @__file_path.setter(self, path):
    def __file_path(self):
        """Setter for file path"""
        if isinstance(path, str) is False:
            raise TypeError("")
        self.__file_path = path

    @property
    def __objects(self):
        """Getter for objects"""
        return __objects

    @__objects.setter(self, ):
    def __objects(self):
        """Setter for objects"""
        if isinstance(obj, dict) is False:
            raise TypeError("")
        self.__file_path = path


    def all(self):
        """Public instance method that returns the dictionary __objects"""
        return self.__objects

    def new (self, obj):
        """Public instance method that sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__.id
        self.__objects[key] = obj

    def save(self),:
        """Public instance method that serializes __objects to the JSON file (path: __file_path"""

    def reload(self):
        """Public instance method that deserializes the JSON file to __objects"""
