#!/usr/bin/python3
"""Unittest for BaseModel"""
from models.base_model import BaseModel
import os
import unittest
import sys
from io import StringIO
import uuid


class TestBaseModel(unittest.TestCase):
    """BaseModel uuid test"""
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1.id, str)
        self.assertTrue(hasattr(bm1, id))
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == '__main__':
    unittest.main()

# Make sure BaseModel was created
# Make sure BaseModel has unique id
# Make sure BaseModel is serializing properly
# Make sure BaseModel updates correctly
# Make sure BaseModel saves correctly
# Check attributes(key/value pairs)
