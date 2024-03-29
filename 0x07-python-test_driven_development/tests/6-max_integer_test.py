#!/usr/bin/python3
"""Creating a unittest  for max_integer([..]) function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Creating a class for the unittest
    it inherits from unnittest.TestCase."""

    def test_ordered_list(self):
        """Creating a test for ordered list."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_list(self):
        """Creating a test for  an unordered list of integers."""
        unordered_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_begginning(self):
        """Checking a for a descending list."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Testing an empty list."""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_one_element_list(self):
        """Testing for a single integer."""
        single = [7]
        self.assertEqual(max_integer(single), 7)

    def test_floats(self):
        """Testing for floats in a list."""
        floats = [1.53, 6.33, -8.56, 14.2, 6.0]
        self.assertEqual(max_integer(floats), 14.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
