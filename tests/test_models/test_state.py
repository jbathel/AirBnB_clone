#!/usr/bin/python3

"""Unittest for State"""
from models.base_model import BaseModel
from models.state import State
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestState(unittest.TestCase):
    """State uuid testing"""
    def test_uuid(self):
        """Test that UUID was created"""
        state1 = State()
        self.assertTrue(hasattr(state1, 'id'))

    def test_uniq_uuid(self):
        """Test that the UUIDs created are unique"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_base_model(self):
        """Test that object created is of BaseModel"""
        state1 = State()
        self.assertIsInstance(state1, State)

    def test_uuid_str(self):
        """Test that id is of type string"""
        state1 = State()
        self.assertIsInstance(state1.id, str)

    def test_created_at(self):
        """Test that objects are created with datetime"""
        state1 = State()
        time.sleep(2)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_create_update_equal(self):
        """Test that created_at and updated_at or equal upon creation"""
        state1 = State()
        self.assertEqual(state1.created_at, state1.updated_at)

    def test_create_update_not_equal(self):
        """Test that created_at datetime is not the same as updated_at"""
        state1 = State()
        time.sleep(2)
        state1.updated_at = datetime.now()
        self.assertNotEqual(state1.created_at, state1.updated_at)

    def test_created_at_exists(self):
        """Test the created_at datetime object exists"""
        state1 = State()
        self.assertTrue(hasattr(state1, 'created_at'))

    def test_updated_at_exists(self):
        """Test that updated_at datetime object exists"""
        state1 = State()
        self.assertTrue(hasattr(state1, 'updated_at'))

    def test_created_at_datetime(self):
        """Test that created_at is a datetime object"""
        state1 = State()
        self.assertTrue(isinstance(state1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is a datetime object"""
        state1 = State()
        self.assertTrue(isinstance(state1.updated_at, datetime))

    def test_base_model_input_dict(self):
        """Test if able to add attiributes using dictionary"""
        attributes = {"id": "1"}
        state1 = State(**attributes)
        self.assertEqual(attributes['id'], state1.id)

if __name__ == '__main__':
    unittest.main()
