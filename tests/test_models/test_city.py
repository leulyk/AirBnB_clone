#!/usr/bin/python3

""" module to test the City class """

import unittest
import io
from unittest.mock import patch
from models.city import City


class TestCity(unittest.TestCase):
    """ class containing unittests for the City class """
    def setUp(self):
        """ sets up instance of the City class for testing """
        self.c = City()
        dct = self.c.to_dict()
        self.c2 = City(**dct)
        self.c2.is_capital = "yes"

    def test_constructor(self):
        """ tests the City constructor with no arguments """
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the City constructor with arguments """
        self.assertTrue(hasattr(self.c2, 'state_id'))
        self.assertTrue(hasattr(self.c2, 'name'))
        self.assertTrue(hasattr(self.c2, 'id'))
        self.assertTrue(hasattr(self.c2, 'created_at'))
        self.assertTrue(hasattr(self.c2, 'updated_at'))
        self.assertTrue(hasattr(self.c2, 'is_capital'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[City] ({}) {}".format(self.c.id, str(self.c.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.c, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a City instance """
        dct = self.c.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.c).__name__)
