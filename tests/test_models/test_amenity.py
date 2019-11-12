#!/usr/bin/python3

"""Unittest for Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Amenity uuid testing"""
    def test_uuid(self):
        """..."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_base_model(self):
        """..."""
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, Amenity)

    def test_uuid_str(self):
        """..."""
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.id, str)

    def test_created_at(self):
        """..."""
        amenity1 = Amenity()
        time.sleep(2)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_create_update_equal(self):
        """..."""
        amenity1 = Amenity()
        self.assertEqual(amenity1.created_at, amenity1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        amenity1 = Amenity()
        time.sleep(2)
        amenity1.updated_at = datetime.now()
        self.assertNotEqual(amenity1.created_at, amenity1.updated_at)

    def test_created_at_exists(self):
        """..."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        amenity1 = Amenity()
        self.assertTrue(isinstance(amenity1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        amenity1 = Amenity()
        self.assertTrue(isinstance(amenity1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        amenity1 = Amenity(**attributes)
        self.assertEqual(attributes['id'], amenity1.id)

if __name__ == '__main__':
    unittest.main()