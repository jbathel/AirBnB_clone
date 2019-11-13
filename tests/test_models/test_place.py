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


class TestPlaceModel(unittest.TestCase):
    """Place uuid testing"""

    def setUp(self):
        """Set up Place Objects for testing"""
        self.place1 = Place()
        time.sleep(1)
        self.place2 = Place()

    def test_uuid(self):
        """Test that UUID was created"""
        self.assertTrue(hasattr(self.place1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_place_model(self):
        """Test that object created is of Place"""
        self.assertIsInstance(self.place1, Place)

    def test_place_model_BaseModel(self):
        """Test that object created is of BaseModel"""
        self.assertIsInstance(self.place1, BaseModel)

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.place1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        self.assertNotEqual(self.place1.created_at, self.place2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.place1.created_at, self.place1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.place1.updated_at = datetime.now()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        self.assertTrue(hasattr(self.place1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        self.assertTrue(hasattr(self.place1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertTrue(isinstance(self.place1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.place1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.place1 = Place(**attributes)
        self.assertEqual(attributes['id'], self.place1.id)

    def tearDown(self):
        """Tear down Place Objects for testing"""
        del self.place1
        del self.place2

    def test_class_attribute(self):
        """Test class attribute"""
        self.assertTrue(hasattr(self.place1, 'name'))
        self.assertTrue(isinstance(self.place1.name, str))
        self.assertTrue(self.place1.name == '')
        # Place.city_id =
        # Place.user_id =
        Place.name = 'Hayward'
        Place.description = 'Melting Pot'
        Place.number_rooms = 4
        Place.number_bathrooms = 4
        Place.max_guest = 8
        Place.price_by_night = 200
        Place.latitude = 37.6688
        Place.longitude = 122.0810
        # Place.amenity_ids =
        self.assertEqual(self.place1.name, 'Hayward')
        self.assertTrue(isinstance(self.place1.name, str))
        self.assertEqual(self.place1.description, 'Melting Pot')
        self.assertTrue(isinstance(self.place1.description, str))
        self.assertEqual(self.place1.number_rooms, 4)
        self.assertTrue(isinstance(self.place1.number_rooms, int))
        self.assertEqual(self.place1.number_bathrooms, 4)
        self.assertTrue(isinstance(self.place1.number_bathrooms, int))
        self.assertEqual(self.place1.max_guest, 8)
        self.assertTrue(isinstance(self.place1.max_guest, int))
        self.assertEqual(self.place1.price_by_night, 200)
        self.assertTrue(isinstance(self.place1.price_by_night, int))
        self.assertEqual(self.place1.latitude, 37.6688)
        self.assertTrue(isinstance(self.place1.latitude, float))
        self.assertEqual(self.place1.longitude, 122.0810)
        self.assertTrue(isinstance(self.place1.longitude, float))
        self.assertEqual(self.place1.name, self.place2.name)

if __name__ == '__main__':
    unittest.main()
