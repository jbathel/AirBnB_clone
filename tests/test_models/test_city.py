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


class TestBaseModel(unittest.TestCase):
    """City uuid testing"""
    def test_uuid(self):
        """Test that UUID was created"""
        city1 = City()
        self.assertTrue(hasattr(city1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        city1 = City()
        self.assertIsInstance(city1, City)

    def test_uuid_str(self):
        """Test that id is of type string"""
        city1 = City()
        self.assertIsInstance(city1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        city1 = City()
        time.sleep(2)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        city1 = City()
        self.assertEqual(city1.created_at, city1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        city1 = City()
        time.sleep(2)
        city1.updated_at = datetime.now()
        self.assertNotEqual(city1.created_at, city1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        city1 = City()
        self.assertTrue(hasattr(city1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        city1 = City()
        self.assertTrue(hasattr(city1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        city1 = City()
        self.assertTrue(isinstance(city1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        city1 = City()
        self.assertTrue(isinstance(city1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        city1 = City(**attributes)
        self.assertEqual(attributes['id'], city1.id)

if __name__ == '__main__':
    unittest.main()
