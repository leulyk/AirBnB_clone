#!/usr/bin/python3

""" module to test the file storage engine """

import unittest
from unittest.mock import patch
import io
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ class providing unit tests for the FileStorage class """
    def setUp(self):
        """ initializes a FileStorage instance for testing """
        self.test_storage = FileStorage()

    def test_check_attributes(self):
        """ checks for mandatory attributes in the FileStorage class """
        self.assertTrue(hasattr(self.test_storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.test_storage, "_FileStorage__objects"))
