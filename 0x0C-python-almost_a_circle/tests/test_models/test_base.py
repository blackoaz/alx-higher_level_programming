#!/usr/bin/python3
"""test module for Bae class"""

import unittest
Base = __import__("models.base").base.Base


class TestBase(unittest.TestCase):
    """unittest for base class"""

    def test_baseInitialization(self):
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id,2 )

    def test_id(self):
        base = Base(50)
        self.assertEqual(base.id, 50)

if __name__ == '__main__':
    unittest.main()
