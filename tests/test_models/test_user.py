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
        """..."""
        user1 = User()
        self.assertTrue(hasattr(user1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_base_model(self):
        """..."""
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_uuid_str(self):
        """..."""
        user1 = User()
        self.assertIsInstance(user1.id, str)

    def test_created_at(self):
        """..."""
        user1 = User()
        time.sleep(2)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_create_update_equal(self):
        """..."""
        user1 = User()
        self.assertEqual(user1.created_at, user1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        user1 = User()
        time.sleep(2)
        user1.updated_at = datetime.now()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_created_at_exists(self):
        """..."""
        user1 = User()
        self.assertTrue(hasattr(user1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        user1 = User()
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        user1 = User()
        self.assertTrue(isinstance(user1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        user1 = User()
        self.assertTrue(isinstance(user1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        user1 = User(**attributes)
        self.assertEqual(attributes['id'], user1.id)

if __name__ == '__main__':
    unittest.main()
