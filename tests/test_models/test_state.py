#!/usr/bin/python3
""" Unittests for models/state.py """

import unittest
from models.state import State


class test_tate(unittest.TestCase):
    """ testing instances """

    def test_name(self):
        state = State()
        state.name = 'Lagos'
        self.assertEqual('Lagos', state.name)
