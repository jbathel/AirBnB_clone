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


class TestAmenityModel(unittest.TestCase):
    """Amenity uuid testing"""

    def setUp(self):
        """Set up Amenity Objects for testing"""
        self.amenity1 = Amenity()
        time.sleep(1)
        self.amenity2 = Amenity()

    def test_uuid(self):
        """Test if Amenity has attribute id"""
        self.assertTrue(hasattr(self.amenity1, 'id'))

    def test_uniq_uuid(self):
        """Test that Ameinty has unique id upon creation"""
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_amenity_model(self):
        """Test that object created is Amenity"""
        self.assertIsInstance(self.amenity1, Amenity)

    def test_amenity_model_of_BaseModel(self):
        """Test that object created is Amenity"""
        self.assertTrue(issubclass(type(self.amenity1), BaseModel))

    def test_uuid_str(self):
        """Test that id for Amenity is type string"""
        self.assertIsInstance(self.amenity1.id, str)

    def test_created_at(self):
        """Test that datetime objects are not equal"""
        self.assertNotEqual(self.amenity1.created_at, self.amenity2.created_at)

    def test_create_update_equal(self):
        """Test datetime objects created and updated are equal upon creation"""
        self.assertEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_create_update_not_equal(self):
        """Test that when updated the datetime objects are not equal"""
        self.amenity1.updated_at = datetime.now()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_created_at_exists(self):
        """Test for created_at attribute existing"""
        self.assertTrue(hasattr(self.amenity1, 'created_at'))

    def test_updated_at_exists(self):
        """Test for updated_at attribute existing"""
        self.assertTrue(hasattr(self.amenity1, 'updated_at'))

    def test_created_at_datetime(self):
        """Tests that created_at is a datetime object"""
        self.assertTrue(isinstance(self.amenity1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Tests that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.amenity1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.amenity1 = Amenity(**attributes)
        self.assertEqual(attributes['id'], self.amenity1.id)

    def test_to_dict_attr(self):
        """ created_at, updated_at values """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.amenity1.to_dict()
        self.assertEqual(dictionary["created_at"],
                         self.amenity1.created_at.strftime(time_format))
        self.assertEqual(dictionary["updated_at"],
                         self.amenity1.updated_at.strftime(time_format))
        self.assertEqual(dictionary["__class__"], "Amenity")
        self.assertEqual(type(dictionary["created_at"]), str)
        self.assertEqual(type(dictionary["updated_at"]), str)

    def test_str(self):
        """Test output string of the objects"""
        string = "[{}] ({}) {}".format(
            self.amenity1.__class__.__name__,
            self.amenity1.id, self.amenity1.__dict__)
        self.assertEqual(str(self.amenity1), string)

    def tearDown(self):
        """Tear down Amenity Objects for testing"""
        del self.amenity1
        del self.amenity2


if __name__ == '__main__':
    unittest.main()
