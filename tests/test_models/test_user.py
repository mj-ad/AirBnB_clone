#!/usr/bin/python3
""" Unittests for models/user.py """

import unittest
from models.user import User


class test_user(unittest.TestCase):
    """ testing class instances """

    def test_email(self):
        user = User()
        user.email = 'ade@gmail.com'
        self.assertEqual('ade@gmail.com', user.email)

    def test_password(self):
        user = User()
        user.password = 'pass'
        self.assertEqual('pass', user.password)

    def test_fname(self):
        user = User()
        user.first_name = 'ade'
        self.assertEqual('ade', user.first_name)

    def test_lname(self):
        user = User()
        user.last_name = 'adeo'
        self.assertEqual('adeo', user.last_name)
