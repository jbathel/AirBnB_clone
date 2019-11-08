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

    def setUp(self):
        """Set up BaseModel Objects for testing"""
        self.basemodel1 = BaseModel()
        time.sleep(1)
        self.basemodel2 = BaseModel()

    def test_uuid(self):
        """Test that UUID was created"""
        self.assertTrue(hasattr(self.basemodel1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.basemodel1.id, self.basemodel2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        self.assertIsInstance(self.basemodel1, BaseModel)

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.basemodel1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        time.sleep(2)
        self.assertNotEqual(self.basemodel1.created_at, self.basemodel2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.basemodel1.created_at, self.basemodel1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.basemodel1 = BaseModel()
        time.sleep(2)
        self.basemodel1.updated_at = datetime.now()
        self.assertNotEqual(self.basemodel1.created_at, self.basemodel1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        self.basemodel1 = BaseModel()
        self.assertTrue(hasattr(self.basemodel1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        self.assertTrue(hasattr(self.basemodel1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertTrue(isinstance(self.basemodel1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.basemodel1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.basemodel1 = BaseModel(**attributes)
        self.assertEqual(attributes['id'], self.basemodel1.id)

    def tearDown(self):
        """Tear dowm BaseModel Objects for testing"""
        del self.basemodel1
        del self.basemodel2

if __name__ == '__main__':
    unittest.main()
