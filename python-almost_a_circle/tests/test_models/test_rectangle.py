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

    def test_to_dict(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        dict1 = {
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 4,
                "id": 5
                }
        self.assertEqual(dict1, rect1.to_dictionary())

    def test_update_rect(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(6)
        self.assertEqual(6, rect1.id)

    def test_update_two(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(6, 7)
        self.assertEqual(6, rect1.id)
        self.assertEqual(7, rect1.width)

    def test_update_three(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(6, 7, 8)
        self.assertEqual(6, rect1.id)
        self.assertEqual(7, rect1.width)
        self.assertEqual(8, rect1.height)

    def test_update_five(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(6, 7, 8, 9, 1)
        self.assertEqual(6, rect1.id)
        self.assertEqual(7, rect1.width)
        self.assertEqual(8, rect1.height)
        self.assertEqual(9, rect1.x)
        self.assertEqual(1, rect1.y)

    def test_create_dir(self):
        dict1 = {
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 4,
                "id": 5
                }
        rect1 = Rectangle.create(**dict1)
        self.assertEqual(3, rect1.x)

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(str, type(string))

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_to_empty_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect1])
        list1 = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list1[0]))
