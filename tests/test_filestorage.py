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
    """..."""

    @classmethod
    def setUp(self):
        """..."""
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def test_FileStorage_file_path_exist(self):
        """..."""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_FileStorage__objects_exist(self):
        """..."""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_FileStorage_file_path_value(self):
        """..."""
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')

    def test_FileStorage__objects_value(self):
        """..."""
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_FileStorage_file_path_type(self):
        """..."""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str))

    def test_FileStorage__objects_value(self):
        """..."""
        self.assertTrue(isinstance(FileStorage._FileStorage__objects, dict))


    def test_FileStorage_all(self):
        """Test the all() method in class FileStorage"""
        storage = FileStorage()
        FileStorage._FileStorage__objects = {'test':'Hi'}
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





if __name__ == '__main__':
    unittest.main()
