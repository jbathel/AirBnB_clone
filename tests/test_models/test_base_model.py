#!/usr/bin/python3

"""Unittest for BaseModel"""
from datetime import datetime
from io import StringIO
from models.base_model import BaseModel
import json
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

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.basemodel1.id, str)

    def test_uuid_str_len(self):
        """Test the length of id"""
        self.assertEqual(len(self.basemodel1.id), 36)

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.basemodel1.id, self.basemodel2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        self.assertIsInstance(self.basemodel1, BaseModel)

    def test_created_at(self):
        """Test that multiple objects are created with  unique datetime"""
        self.assertNotEqual(self.basemodel1.created_at,
                            self.basemodel2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.basemodel1.created_at,
                         self.basemodel1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.basemodel1.updated_at = datetime.now()
        self.assertNotEqual(self.basemodel1.created_at,
                            self.basemodel1.updated_at)

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

    def test_to_dict_attr(self):
        """ created_at, updated_at values """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.basemodel1.to_dict()
        self.assertEqual(
            dictionary["created_at"],
            self.basemodel1.created_at.strftime(time_format))
        self.assertEqual(
            dictionary["updated_at"],
            self.basemodel1.updated_at.strftime(time_format))
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(type(dictionary["created_at"]), str)
        self.assertEqual(type(dictionary["updated_at"]), str)

    def test_to_dict(self):
        """ dictionary conversion """
        self.basemodel1.name = "Holberton"
        self.basemodel1.my_number = 89
        my_json = self.basemodel1.to_dict()
        self.assertEqual(my_json["id"], self.basemodel1.id)
        self.assertEqual(my_json["name"], "Holberton")
        self.assertEqual(my_json["my_number"], 89)
        self.assertEqual(my_json["__class__"], "BaseModel")
        self.assertEqual(my_json["created_at"],
                         self.basemodel1.created_at.isoformat())
        self.assertEqual(my_json["updated_at"],
                         self.basemodel1.updated_at.isoformat())

    def test_type(self):
        """ testing the type of the attributes """
        self.assertTrue(type(self.basemodel1), BaseModel)
        self.basemodel1.name = "Holberton"
        self.assertEqual(self.basemodel1.name, "Holberton")
        self.assertTrue(type(self.basemodel1.name), str)
        self.basemodel1.my_number = 89
        self.assertEqual(self.basemodel1.my_number, 89)
        self.assertTrue(type(self.basemodel1.my_number), int)
        self.assertEqual(type(self.basemodel1.id), str)
        self.assertEqual(type(self.basemodel1.created_at), datetime)
        self.assertEqual(type(self.basemodel1.updated_at), datetime)

    def test_str(self):
        """Test output string of the objects"""
        string = "[{}] ({}) {}".format(
            self.basemodel1.__class__.__name__,
            self.basemodel1.id, self.basemodel1.__dict__)
        self.assertEqual(str(self.basemodel1), string)

    def tearDown(self):
        """Tear dowm BaseModel Objects for testing"""
        del self.basemodel1
        del self.basemodel2


if __name__ == '__main__':
    unittest.main()
