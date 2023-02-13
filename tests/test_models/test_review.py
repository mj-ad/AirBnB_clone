#!/usr/bin/python3
""" Unittests for models/review.py """

import unittest
from models.review import Review


class test_review(unittest.TestCase):
    """ testing instances """

    def test_text(self):
        r = Review()
        r.text = 'Perfect'
        self.assertEqual('Perfect', r.text)
