#!/usr/bin/python3

""" module to test the User class """

import unittest
import io
from unittest.mock import patch
from models.user import User


class TestUser(unittest.TestCase):
    """ class containing unittests for the User class """
    def setUp(self):
        """ sets up instance of the User class for testing """
        self.u = User()
        dct = self.u.to_dict()
        self.u2 = User(**dct)

    def test_constructor(self):
        """ tests the User constructor with no arguments """
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))

    def test_constructor_kwargs(self):
        """ tests the User constructor with arguments """
        self.assertTrue(hasattr(self.u2, 'id'))
        self.assertTrue(hasattr(self.u2, 'created_at'))
        self.assertTrue(hasattr(self.u2, 'updated_at'))
        self.assertTrue(hasattr(self.u2, 'first_name'))
        self.assertTrue(hasattr(self.u2, 'last_name'))
        self.assertTrue(hasattr(self.u2, 'email'))
        self.assertTrue(hasattr(self.u2, 'password'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[User] ({}) {}".format(self.u.id, str(self.u.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.u, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a User instance """
        dct = self.u.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.u).__name__)
