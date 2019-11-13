#!/usr/bin/python3

"""Unittest for BaseModel"""
from datetime import datetime
from io import StringIO
from models.base_model import BaseModel
import models
import os
import sys
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """BaseModel uuid testing"""
    def test_uuid(self):
        """Test that UUID was created"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)

    def test_uuid_str(self):
        """Test that id is of type string"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        bm1 = BaseModel()
        time.sleep(2)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        bm1 = BaseModel()
        time.sleep(2)
        bm1.updated_at = datetime.now()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        bm1 = BaseModel()
        self.assertTrue(isinstance(bm1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        bm1 = BaseModel()
        self.assertTrue(isinstance(bm1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        bm1 = BaseModel(**attributes)
        self.assertEqual(attributes['id'], bm1.id)

if __name__ == '__main__':
    unittest.main()
