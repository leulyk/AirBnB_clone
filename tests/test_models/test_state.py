#!/usr/bin/python3

""" module to test the State class """

import unittest
import io
from unittest.mock import patch
from models.state import State


class TestState(unittest.TestCase):
    """ class containing unittests for the State class """
    def setUp(self):
        """ sets up instance of the State class for testing """
        self.st = State()
        dct = self.st.to_dict()
        self.st2 = State(**dct)

    def test_constructor(self):
        """ tests the State constructor with no arguments """
        self.assertTrue(hasattr(self.st, 'name'))
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the State constructor with arguments """
        self.assertTrue(hasattr(self.st2, 'name'))
        self.assertTrue(hasattr(self.st2, 'id'))
        self.assertTrue(hasattr(self.st2, 'created_at'))
        self.assertTrue(hasattr(self.st2, 'updated_at'))

    def test_str(self):
        """ test the __str__ magic method """
        expected = "[State] ({}) {}".format(self.st.id, str(self.st.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake:
            print(self.st, end="")
            output = fake.getvalue()
            self.assertEqual(output, expected)

    def test_to_dict(self):
        """ tests dictionary representation of a State instance """
        dct = self.st.to_dict()
        self.assertTrue('__class__' in dct.keys())
        self.assertEqual(dct['__class__'], type(self.st).__name__)
