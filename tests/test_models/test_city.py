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
        """..."""
        city1 = City()
        self.assertTrue(hasattr(city1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_base_model(self):
        """..."""
        city1 = City()
        self.assertIsInstance(city1, City)

    def test_uuid_str(self):
        """..."""
        city1 = City()
        self.assertIsInstance(city1.id, str)

    def test_created_at(self):
        """..."""
        city1 = City()
        time.sleep(2)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_create_update_equal(self):
        """..."""
        city1 = City()
        self.assertEqual(city1.created_at, city1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        city1 = City()
        time.sleep(2)
        city1.updated_at = datetime.now()
        self.assertNotEqual(city1.created_at, city1.updated_at)

    def test_created_at_exists(self):
        """..."""
        city1 = City()
        self.assertTrue(hasattr(city1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        city1 = City()
        self.assertTrue(hasattr(city1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        city1 = City()
        self.assertTrue(isinstance(city1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        city1 = City()
        self.assertTrue(isinstance(city1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        city1 = City(**attributes)
        self.assertEqual(attributes['id'], city1.id)

if __name__ == '__main__':
    unittest.main()
