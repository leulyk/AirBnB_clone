#!/usr/bin/env python3

""" module to test the file storage engine """

import unittest
from unittest.mock import patch
import io
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """ class providing unit tests for the FileStorage class """
    def setUp(self):
        """ initializes a FileStorage instance for testing """
        test_storage = FileStorage()
