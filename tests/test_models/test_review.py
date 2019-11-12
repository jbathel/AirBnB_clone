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
        """..."""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'id'))

    def test_uniq_uuid(self):
        """..."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_base_model(self):
        """..."""
        review1 = Review()
        self.assertIsInstance(review1, Review)

    def test_uuid_str(self):
        """..."""
        review1 = Review()
        self.assertIsInstance(review1.id, str)

    def test_created_at(self):
        """..."""
        review1 = Review()
        time.sleep(2)
        review2 = Review()
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_create_update_equal(self):
        """..."""
        review1 = Review()
        self.assertEqual(review1.created_at, review1.updated_at)

    def test_create_update_not_equal(self):
        """..."""
        review1 = Review()
        time.sleep(2)
        review1.updated_at = datetime.now()
        self.assertNotEqual(review1.created_at, review1.updated_at)

    def test_created_at_exists(self):
        """..."""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'created_at'))

    def test_updated_at_exists(self):
        """..."""
        review1 = Review()
        self.assertTrue(hasattr(review1, 'updated_at'))

    def test_created_at_datetime(self):
        """..."""
        review1 = Review()
        self.assertTrue(isinstance(review1.created_at, datetime))

    def test_updated_at_datetime(self):
        """..."""
        review1 = Review()
        self.assertTrue(isinstance(review1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """..."""
        attributes = {"id": "1"}
        review1 = Review(**attributes)
        self.assertEqual(attributes['id'], review1.id)

if __name__ == '__main__':
    unittest.main()
