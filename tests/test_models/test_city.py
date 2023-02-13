#!/usr/bin/python3
""" Unittests for models/city.py """

import unittest
from models.city import City


class test_city(unittest.TestCase):
    """ Testing instances """

    def test_name(self):
        c = City()
        c.name = 'Lagos'
        self.assertEqual('Lagos', c.name)
