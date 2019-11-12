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
        """..."""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_base_model(self):
        """..."""
        place1 = Place()
        self.assertIsInstance(place1, Place)

    def test_uuid_str(self):
        """..."""
        place1 = Place()
        self.assertIsInstance(place1.id, str)

    def test_created_at(self):
        """..."""
        place1 = Place()
        time.sleep(2)
        place2 = Place()
        self.assertNotEqual(place1.created_at, place2.created_at)

    def test_create_update_equal(self):
        """..."""
        place1 = Place()
        self.assertEqual(place1.created_at, place1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        place1 = Place()
        time.sleep(2)
        place1.updated_at = datetime.now()
        self.assertNotEqual(place1.created_at, place1.updated_at)

    def test_created_at_exists(self):
        """..."""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        place1 = Place()
        self.assertTrue(isinstance(place1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        place1 = Place()
        self.assertTrue(isinstance(place1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        place1 = Place(**attributes)
        self.assertEqual(attributes['id'], place1.id)

if __name__ == '__main__':
    unittest.main()
