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

    def setUp(self):
        """Set up User Objects for testing"""
        self.user1 = User()
        time.sleep(1)
        self.user2 = User()

    def test_uuid(self):
        """Test that UUID was created"""
        self.assertTrue(hasattr(self.user1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_user_model(self):
        """Test that object created is of User"""
        self.assertIsInstance(self.user1, User)

    def test_user_model_BaseModel(self):
        """Test that object created is of BaseModel"""
        self.assertTrue(issubclass(type(self.user1), BaseModel)
                        )

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.user1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        self.assertNotEqual(self.user1.created_at, self.user2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.user1.created_at, self.user1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.user1.updated_at = datetime.now()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        self.assertTrue(hasattr(self.user1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        self.assertTrue(hasattr(self.user1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertTrue(isinstance(self.user1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.user1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.user1 = User(**attributes)
        self.assertEqual(attributes['id'], self.user1.id)

    def test_to_dict_attr(self):
        """ created_at, updated_at values """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.user1.to_dict()
        self.assertEqual(dictionary["created_at"],
                         self.user1.created_at.strftime(time_format))
        self.assertEqual(dictionary["updated_at"],
                         self.user1.updated_at.strftime(time_format))
        self.assertEqual(dictionary["__class__"], 'User')
        self.assertEqual(type(dictionary["created_at"]), str)
        self.assertEqual(type(dictionary["updated_at"]), str)

    def test_str(self):
        """Test output string of the objects"""
        string = "[{}] ({}) {}".format(
            self.user1.__class__.__name__, self.user1.id, self.user1.__dict__)
        self.assertEqual(str(self.user1), string)

    def tearDown(self):
        """Tear down Amenity Objects for testing"""
        del self.user1
        del self.user2


if __name__ == '__main__':
    unittest.main()
