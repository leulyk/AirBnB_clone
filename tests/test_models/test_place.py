#!/usr/bin/python3

""" module to test the Place class """

import unittest
import io
from unittest.mock import patch
from models.place import Place


class TestPlace(unittest.TestCase):
    """ class containing unittests for the Place class """
    def setUp(self):
        """ sets up instance of the Place class for testing """
        self.pl = Place()
        dct = self.pl.to_dict()
        self.pl2 = Place(**dct)

    def test_constructor(self):
        """ tests the Place constructor with no arguments """
        self.assertTrue(hasattr(self.pl, 'city_id'))
        self.assertTrue(hasattr(self.pl, 'user_id'))
        self.assertTrue(hasattr(self.pl, 'name'))
        self.assertTrue(hasattr(self.pl, 'id'))
        self.assertTrue(hasattr(self.pl, 'created_at'))
        self.assertTrue(hasattr(self.pl, 'updated_at'))
        self.assertTrue(hasattr(self.pl, 'description'))
        self.assertTrue(hasattr(self.pl, 'number_rooms'))
        self.assertTrue(hasattr(self.pl, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl, 'max_guest'))
        self.assertTrue(hasattr(self.pl, 'price_by_night'))
        self.assertTrue(hasattr(self.pl, 'latitude'))
        self.assertTrue(hasattr(self.pl, 'longitude'))
        self.assertTrue(hasattr(self.pl, 'amenity_ids'))

    def test_constructor_kwargs(self):
        """ tests the Place constructor with arguments """
        self.assertTrue(hasattr(self.pl2, 'name'))
        self.assertTrue(hasattr(self.pl2, 'created_at'))
        self.assertTrue(hasattr(self.pl2, 'city_id'))
        self.assertTrue(hasattr(self.pl2, 'user_id'))
        self.assertTrue(hasattr(self.pl2, 'id'))
        self.assertTrue(hasattr(self.pl2, 'updated_at'))
        self.assertTrue(hasattr(self.pl2, 'description'))
        self.assertTrue(hasattr(self.pl2, 'number_rooms'))
        self.assertTrue(hasattr(self.pl2, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl2, 'max_guest'))
        self.assertTrue(hasattr(self.pl2, 'price_by_night'))
        self.assertTrue(hasattr(self.pl2, 'latitude'))
        self.assertTrue(hasattr(self.pl2, 'longitude'))
        self.assertTrue(hasattr(self.pl2, 'amenity_ids'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[Place] ({}) {}".format(self.pl.id, str(self.pl.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.pl, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a Place instance """
        dct = self.pl.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.pl).__name__)
