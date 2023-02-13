#!/usr/bin/python3
""" Unittests for models/base_model.py """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_Declarations(unittest.TestCase):
    """ testing declared variables """

    def test_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().created_at)

    def test_updated_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().updated_at)


class Test_Use_of_kwargs(unittest.TestCase):
    """ testing the use kwargs """
    def test_use_of_kwargs(self):
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(type(b1), type(b2))

    def test_b1_and_b1_json(self):
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertNotEqual(type(b1), type(b1_json))

    def test_same_id(self):
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(b2.id, b1.id)


if __name__ == '__main__':
    unittest.main()
