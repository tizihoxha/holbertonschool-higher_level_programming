#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Test class for rectangle"""
    def test_rect_two_args(self):
        rect1 = Rectangle(1, 2)
        self.assertEqual(1, rect1.width)

    def test_rect_three_args(self):
        rect1 = Rectangle(1, 2, 3)
        self.assertEqual(1, rect1.width)

    def test_rect_four_args(self):
        rect1 = Rectangle(5, 2, 6, 4)
        self.assertEqual(6, rect1.x)

    def test_width_str(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle("1", 2)

    def test_height_str(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "2")

    def test_x_str(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, "3")

    def test_y_str(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, 3, "4")

    def test_rect_five_args(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, rect1.id)

    def test_neg_width(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 2)

    def test_neg_height(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 0)

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, -3)

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, 3, -4)

    def test_rect_area(self):
        rect1 = Rectangle(1, 2)
        self.assertEqual(2, rect1.area())

    def test_str(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", rect1.__str__())

    def test_display(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rect1 = Rectangle(1, 2)
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("#\n#\n", capturedOutput.getvalue())

    def test_display_xy(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rect1 = Rectangle(1, 2, 2, 2)
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n  #\n  #\n", capturedOutput.getvalue())

