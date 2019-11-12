#!/usr/bin/python3

"""Unittest for BaseModel"""
from models.base_model import BaseModel
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """BaseModel uuid testing"""
    def test_uuid(self):
        """..."""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_base_model(self):
        """..."""
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)

    def test_uuid_str(self):
        """..."""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """..."""
        bm1 = BaseModel()
        time.sleep(2)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_create_update_equal(self):
        """..."""
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        bm1 = BaseModel()
        time.sleep(2)
        bm1.updated_at = datetime.now()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_created_at_exists(self):
        """..."""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        bm1 = BaseModel()
        self.assertTrue(isinstance(bm1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        bm1 = BaseModel()
        self.assertTrue(isinstance(bm1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        bm1 = BaseModel(**attributes)
        self.assertEqual(attributes['id'], bm1.id)

if __name__ == '__main__':
    unittest.main()
