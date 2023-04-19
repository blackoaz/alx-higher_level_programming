#!/usr/bin/python3
"""Square class unittest
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square unit test methods"""

    def test_initialization_success(self):
        s1 = Square(4)
        s2 = Square(12)
        self.assertEqual(s1.id, 4)
        self.assertEqual(s2.id, 5)

    def test_empty_initialization(self):

        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
