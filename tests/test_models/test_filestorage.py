#!/usr/bin/python3

"""Unittest for FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest
import sys
from io import StringIO
import uuid
import time
from datetime import datetime


class TestFileStorageModel(unittest.TestCase):
    """Unit Tests for FileStorage Model"""

    @classmethod
    def setUp(self):
        """Setup Test Suite"""
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def test_FileStorage_file_path_exist(self):
        """Check that storage exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_FileStorage__objects_exist(self):
        """Check that objects exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_FileStorage_file_path_value(self):
        """Check that file.json has values"""
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')

    def test_FileStorage__objects_value(self):
        """Test that objects craeted have values"""
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_FileStorage_file_path_type(self):
        """Test that file path is a string"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str))

    def test_FileStorage__objects_value(self):
        """Test that objects returned as dictionary"""
        self.assertTrue(isinstance(FileStorage._FileStorage__objects, dict))

    def test_FileStorage_all(self):
        """Test the all() method in class FileStorage"""
        storage = FileStorage()
        FileStorage._FileStorage__objects = {'test': 'Hi'}
        self.assertEqual(FileStorage._FileStorage__objects, storage.all())

    def test_FileStorage_new(self):
        """Test the new() method in class FileStorage"""
        bm1 = BaseModel()
        class_name = bm1.__class__.__name__
        key = class_name + '.' + str(bm1.id)
        storage = FileStorage()
        storage.new(bm1)
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_FileStorage_save_file_exists(self):
        """Test the save() method if file.json exists"""
        bm1 = BaseModel()
        class_name = bm1.__class__.__name__
        key = class_name + '.' + str(bm1.id)
        storage = FileStorage()
        storage.new(bm1)
        storage.save()
        with open('file.json') as file:
            self.assertTrue(isinstance(file.read(), str))

    def test_FileStorage_save_file_key(self):
        """Test the save() method to check contents of file.json """
        bm1 = BaseModel()
        class_name = bm1.__class__.__name__
        key = class_name + '.' + str(bm1.id)
        storage = FileStorage()
        storage.new(bm1)
        storage.save()
        with open('file.json') as file:
            self.assertIn(key, file.read())

    def test_FileStorage_reload_file_exists(self):
        """Test the reload() method to check if file.json exists"""
        bm1 = BaseModel()
        class_name = bm1.__class__.__name__
        key = class_name + '.' + str(bm1.id)
        storage = FileStorage()
        storage.new(bm1)
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_FileStorage_reload_successful(self):
        """Test the reload() method to see if object reloads successfully"""
        FileStorage._FileStorage__objects = {}
        bm1 = BaseModel()
        class_name = bm1.__class__.__name__
        key = class_name + '.' + str(bm1.id)
        storage = FileStorage()
        storage.new(bm1)
        storage.save()
        storage.reload()
        self.assertIn(key, FileStorage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
