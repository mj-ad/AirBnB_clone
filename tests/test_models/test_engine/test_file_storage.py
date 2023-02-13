#!/usr/bin/python3
""" Unittests for models/engine/file_storage.py """

import unittest
from models.engine.file_storage import FileStorage


class test_file(unittest.TestCase):
    """ testing instantiation """

    def test_type(self):
        self.assertEqual(type(FileStorage()), FileStorage)
