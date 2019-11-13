#!/usr/bin/python3

"""Unittest for Review"""
from models.base_model import BaseModel
from models.review import Review
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestReview(unittest.TestCase):
    """Review uuid testing"""

    def setUp(self):
        """Set up Review Objects for testing"""
        self.review1 = Review()
        time.sleep(1)
        self.review2 = Review()

    def test_uuid(self):
        """Test that UUID was created"""
        self.assertTrue(hasattr(self.review1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_review_model(self):
        """Test that object created is of Review"""
        self.assertIsInstance(self.review1, Review)

    def test_review_model_BaseModel(self):
        """Test that object created is of BaseModel"""
        self.assertIsInstance(self.review1, BaseModel)

    def test_uuid_str(self):
        """Test that id is of type string"""
        self.assertIsInstance(self.review1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        self.assertNotEqual(self.review1.created_at, self.review2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        self.assertEqual(self.review1.created_at, self.review1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        self.review1.updated_at = datetime.now()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        self.assertTrue(hasattr(self.review1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        self.assertTrue(hasattr(self.review1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertTrue(isinstance(self.review1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertTrue(isinstance(self.review1.updated_at, datetime))

    def test_review_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        self.review1 = Review(**attributes)
        self.assertEqual(attributes['id'], self.review1.id)

    def test_class_attribute(self):
        """Test class attribute"""
        self.assertTrue(hasattr(self.review1, 'text'))
        self.assertTrue(isinstance(self.review1.text, str))
        self.assertTrue(self.review1.text == '')
        # place_id =
        # user_id =
        Review.text = 'Fabulous!'
        self.assertEqual(self.review1.text, 'Fabulous!')
        self.assertTrue(isinstance(self.review1.text, str))

if __name__ == '__main__':
    unittest.main()
