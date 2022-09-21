#!/usr/bin/python3
"""Unitesting for max integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_maximum_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def text_maximum_beggining(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_maximum_middle(self):
        self.assertEqual(max_integer([2, 3, 4, 1]), 4)

    def test_neg(self)
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_negative_all(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), 4)

    def test_self(self):
        self.assertEqual(max_integer([1], 1)

if __name__== "__main__":
   unittest.main()

