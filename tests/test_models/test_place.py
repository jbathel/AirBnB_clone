#!/usr/bin/python3

"""Unittest for Place"""
from models.base_model import BaseModel
from models.place import Place
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Place uuid testing"""
    def test_uuid(self):
        """Test that UUID was created"""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        place1 = Place()
        self.assertIsInstance(place1, Place)

    def test_uuid_str(self):
        """Test that id is of type string"""
        place1 = Place()
        self.assertIsInstance(place1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        place1 = Place()
        time.sleep(2)
        place2 = Place()
        self.assertNotEqual(place1.created_at, place2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        place1 = Place()
        self.assertEqual(place1.created_at, place1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        place1 = Place()
        time.sleep(2)
        place1.updated_at = datetime.now()
        self.assertNotEqual(place1.created_at, place1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        place1 = Place()
        self.assertTrue(isinstance(place1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        place1 = Place()
        self.assertTrue(isinstance(place1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        place1 = Place(**attributes)
        self.assertEqual(attributes['id'], place1.id)

if __name__ == '__main__':
    unittest.main()
