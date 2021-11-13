
""" module to test the BaseModel class """

import unittest
from models.base_model import BaseModel
from models import storage
from os import remove, path


class TestBaseModel(unittest.TestCase):
    """ class containing unittests for the BaseModel class """
    def setUp(self):
        """ sets up instances of BaseModel for testing """
        self.model1 = BaseModel()
        self.model2 = BaseModel(**{'id': '1456-8912-1289', 'name': 'MyModel'})

    def tearDown(self):
        """ cleans up the JSON file """
        if path.exists("file.json"):
            remove("file.json")

    def test_constructor_no_arg(self):
        """ tests the BaseModel constructor with no argument """
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertTrue(hasattr(self.model1, 'updated_at'))

    def test_constructor_kwargs(self):
        """ tests the BaseModel constructor with a dictionary argument """
        self.assertTrue(hasattr(self.model2, 'id'))
        self.assertTrue(hasattr(self.model2, 'name'))
        self.assertFalse(hasattr(self.model2, 'created_at'))
        self.assertFalse(hasattr(self.model2, 'updated_at'))

    def test_unique_id(self):
        """ tests if unique ids are generated for each instance """
        ids = []
        for i in range(100):
            model = BaseModel()
            ids.append(model.id)
        self.assertEqual(len(ids), len(set(ids)))
