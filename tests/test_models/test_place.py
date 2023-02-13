#!/usr/bin/python3
""" Unittests for models/place.py """

import unittest
from models.place import Place


class test_place(unittest.TestCase):
    """ testing instances """

    def test_longitude_and_latitude(self):
        p = Place()
        p.latitude = 8.0
        p.longitude = 7.5
        self.assertEqual(8.0, p.latitude)
        self.assertEqual(7.5, p.longitude)

    def test_itinery(self):
        p = Place()
        p.max_guest=7
        p.number_rooms=90
        p.number_bathrooms=180
        p.price_by_night=70
        self.assertEqual(7, p.max_guest)
        self.assertEqual(90, p.number_rooms)
        self.assertEqual(180, p.number_bathrooms)
        self.assertEqual(70, p.price_by_night)
