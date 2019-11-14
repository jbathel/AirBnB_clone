#!/usr/bin/python3

"""Unittest for City"""
from models.base_model import BaseModel
from models.city import City
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestCityModel(unittest.TestCase):
    """City uuid testing"""

    def setUp(self):
        """Set up City Objects for testing"""
        self.city1 = City()
        time.sleep(1)
        self.city2 = City()

    def test_class_attribute(self):
        """Test class attribute"""
        self.assertTrue(hasattr(self.city1, 'name'))
        self.assertTrue(isinstance(self.city1.name, str))
        self.assertTrue(self.city1.name == '')
        City.name = 'Santa Barbara'
        self.assertEqual(self.city1.name, 'Santa Barbara')
        self.assertEqual(self.city1.name, self.city2.name)

    def test_uuid(self):
        """Test that UUID was created"""
        self.assertTrue(hasattr(self.city1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_city_model(self):
        """Test that object created is of City"""
        self.assertIsInstance(self.city1, City)

    def test_city_model_BaseModel(self):
        """Test that object created is of BaseModel"""
        self.assertTrue(issubclass(type(self.city1), BaseModel))

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.city1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        self.assertNotEqual(self.city1.created_at, self.city2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.city1.created_at, self.city1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.city1.updated_at = datetime.now()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        self.assertTrue(hasattr(self.city1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        self.assertTrue(hasattr(self.city1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertTrue(isinstance(self.city1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.city1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.city1 = City(**attributes)
        self.assertEqual(attributes['id'], self.city1.id)

    def test_to_dict_attr(self):
        """ created_at, updated_at values """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.city1.to_dict()
        self.assertEqual(dictionary["created_at"],
                         self.city1.created_at.strftime(time_format))
        self.assertEqual(dictionary["updated_at"],
                         self.city1.updated_at.strftime(time_format))
        self.assertEqual(dictionary["__class__"], "City")
        self.assertEqual(type(dictionary["created_at"]), str)
        self.assertEqual(type(dictionary["updated_at"]), str)

    def test_str(self):
        """Test output string of the objects"""
        string = "[{}] ({}) {}".format(
            self.city1.__class__.__name__, self.city1.id, self.city1.__dict__)
        self.assertEqual(str(self.city1), string)


if __name__ == '__main__':
    unittest.main()
