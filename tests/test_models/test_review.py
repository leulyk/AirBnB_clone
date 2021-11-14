#!/usr/bin/python3

""" module to test the Review class """

import unittest
import io
from unittest.mock import patch
from models.review import Review


class TestReview(unittest.TestCase):
    """ class containing unittests for the Review class """
    def setUp(self):
        """ sets up instance of the Review class for testing """
        self.rv = Review()
        dct = self.rv.to_dict()
        self.rv2 = Review(**dct)

    def test_constructor(self):
        """ tests the Review constructor with no arguments """
        self.assertTrue(hasattr(self.rv, 'place_id'))
        self.assertTrue(hasattr(self.rv, 'user_id'))
        self.assertTrue(hasattr(self.rv, 'text_id'))
        self.assertTrue(hasattr(self.rv, 'id'))
        self.assertTrue(hasattr(self.rv, 'created_at'))
        self.assertTrue(hasattr(self.rv, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the Review constructor with arguments """
        self.assertTrue(hasattr(self.rv2, 'place_id'))
        self.assertTrue(hasattr(self.rv2, 'user_id'))
        self.assertTrue(hasattr(self.rv2, 'text_id'))
        self.assertTrue(hasattr(self.rv2, 'id'))
        self.assertTrue(hasattr(self.rv2, 'created_at'))
        self.assertTrue(hasattr(self.rv2, 'updated_at'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[Review] ({}) {}".format(self.rv.id, str(self.rv.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.rv, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a Review instance """
        dct = self.rv.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.rv).__name__)
