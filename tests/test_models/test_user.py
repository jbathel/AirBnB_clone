#!/usr/bin/python3

"""Unittest for User"""
from models.base_model import BaseModel
from models.user import User
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """User uuid testing"""
    def test_uuid(self):
        """Test that UUID was created"""
        user1 = User()
        self.assertTrue(hasattr(user1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_uuid_str(self):
        """Test that id is of type string"""
        user1 = User()
        self.assertIsInstance(user1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        user1 = User()
        time.sleep(2)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        user1 = User()
        self.assertEqual(user1.created_at, user1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        user1 = User()
        time.sleep(2)
        user1.updated_at = datetime.now()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        user1 = User()
        self.assertTrue(hasattr(user1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        user1 = User()
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        user1 = User()
        self.assertTrue(isinstance(user1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        user1 = User()
        self.assertTrue(isinstance(user1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        user1 = User(**attributes)
        self.assertEqual(attributes['id'], user1.id)

if __name__ == '__main__':
    unittest.main()
