#!/usr/bin/python3
""" Unittests for models/amenity.py """

import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """ testing instances """

    def test_name(self):
        a = Amenity()
        a.name = 'Water'
        self.assertEqual('Water', a.name)
