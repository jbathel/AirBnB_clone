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
    def test_uuid(self):
        """Test that UUID was created"""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_review_model(self):
        """Test that object created is of BaseModel"""
        review1 = Review()
        self.assertIsInstance(review1, Review)

    def test_uuid_str(self):
        """Test that id is of type string"""
        review1 = Review()
        self.assertIsInstance(review1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        review1 = Review()
        time.sleep(2)
        review2 = Review()
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        review1 = Review()
        self.assertEqual(review1.created_at, review1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        review1 = Review()
        time.sleep(2)
        review1.updated_at = datetime.now()
        self.assertNotEqual(review1.created_at, review1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        review1 = Review()
        self.assertTrue(isinstance(review1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        review1 = Review()
        self.assertTrue(isinstance(review1.updated_at, datetime))

    def test_review_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        review1 = Review(**attributes)
        self.assertEqual(attributes['id'], review1.id)

if __name__ == '__main__':
    unittest.main()
