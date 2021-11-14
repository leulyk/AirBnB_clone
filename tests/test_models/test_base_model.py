#!/usr/bin/python3

""" module to test the BaseModel class """

import unittest
import io
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from os import remove, path
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ class containing unittests for the BaseModel class """
    def setUp(self):
        """ sets up instances of BaseModel for testing """
        self.model1 = BaseModel()
        dct = self.model1.to_dict()
        self.model2 = BaseModel(**dct)
        self.model2.name = "Leul"

    def tearDown(self):
        """ cleans up the JSON file """
        if path.exists("file.json"):
            remove("file.json")

    def test_constructor_no_arg(self):
        """ tests the BaseModel constructor with no argument """
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertTrue(type(self.model1.id), str)
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertTrue(hasattr(self.model1, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the BaseModel constructor with a dictionary argument """
        self.assertTrue(hasattr(self.model2, 'id'))
        self.assertTrue(hasattr(self.model2, 'name'))
        self.assertTrue(hasattr(self.model2, 'created_at'))
        self.assertTrue(hasattr(self.model2, 'updated_at'))
        self.assertTrue(self.model2.__class__ not in self.model2.__dict__)

    def test_unique_id(self):
        """ tests if unique ids are generated for each instance """
        ids = []
        for i in range(100):
            model = BaseModel()
            ids.append(model.id)
        self.assertEqual(len(ids), len(set(ids)))

    def test_save(self):
        """ tests the save method """
        oldtime = self.model1.updated_at
        self.model1.save()
        newtime = self.model1.updated_at
        self.assertNotEqual(oldtime, newtime)

    def test_to_dict(self):
        """ tests dictionary representation of a BaseModel instance """
        dct = self.model1.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.model1).__name__)
        self.assertEqual(dct['created_at'], self.model1.created_at.isoformat())
        self.assertEqual(dct['updated_at'], self.model1.updated_at.isoformat())

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[{}] ({}) {}".format(type(self.model1).__name__,
                                         self.model1.id,
                                         str(self.model1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.model1, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)
