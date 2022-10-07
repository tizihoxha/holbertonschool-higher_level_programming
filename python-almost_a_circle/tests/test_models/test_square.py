#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for square"""
    def test_square_one_arg(self):
        square1 = Square(1)
        square2 = Square(2)
        self.assertEqual(square1.id, square2.id - 1)

    def test_square_two_args(self):
        square1 = Square(1, 3)
        square2 = Square(2, 4)
        self.assertEqual(square1.id, square2.id - 1)

    def test_square_three_arg(self):
        square1 = Square(1, 2, 3)
        square2 = Square(2, 3, 4)
        self.assertEqual(square1.id, square2.id - 1)
