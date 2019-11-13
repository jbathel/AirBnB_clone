#!/usr/bin/python3
"""
This is a module for File Storage
"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """File Storage Model"""

    __file_path = 'file.json'  # path to JSON file
    __objects = {}  # <class name>.id

    def all(self):
        """Public instance method that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Public instance method that sets in __objects
        the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = class_name + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Public instance method that serializes __objects
        to the JSON file (path: __file_path"""
        dictionary = {}
        for obj_id, obj in self.__objects.items():
            dictionary[obj_id] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(dictionary, json_file)

    def reload(self):
        """Public instance method that deserializes
        the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r',
                      encoding='utf-8') as json_file:
                for obj_id, obj in (json.load(json_file)).items():
                    obj = eval(obj['__class__'])(**(obj))
                    self.__objects[obj_id] = obj
        except:
            pass
