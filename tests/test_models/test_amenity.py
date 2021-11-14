#!/usr/bin/python3

""" module to test the amenity class """

import unittest
import io
from unittest.mock import patch
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ class containing unittests for the Amenity class """
    def setUp(self):
        """ sets up instance of the Amenity class for testing """
        self.am = Amenity()
        dct = self.am.to_dict()
        self.am2 = Amenity(**dct)

    def test_constructor(self):
        """ tests the Amenity constructor with no arguments """
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'name'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the Amenity constructor with arguments """
        self.assertTrue(hasattr(self.am2, 'name'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[Amenity] ({}) {}".format(self.am.id,
                                              str(self.am.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.am, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a Amenity instance """
        dct = self.am.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.am).__name__)
