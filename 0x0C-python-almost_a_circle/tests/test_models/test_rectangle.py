#!/usr/bin/python3
"""Unittest for rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle unittest class"""

    def test_initialization(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.id, Rectangle._Base__nb_objects)
        r1 = Rectangle(1, 4)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)


if __name__ == '__main__':
    unittest.main()
