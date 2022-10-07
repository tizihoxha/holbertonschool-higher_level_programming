#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for square"""
    def test_square_one_arg(self):
        square1 = Square(1)
        self.assertEqual(square1.size, 1)

    def test_square_two_args(self):
        square1 = Square(1, 3)
        self.assertEqual(square1.x, 3)

    def test_square_three_arg(self):
        square1 = Square(1, 2, 3)
        self.assertEqual(square1.y, 3)

    def test_square_four_arg(self):
        square1 = Square(1, 2, 3, 4)
        self.assertEqual(square1.size, 1)

    def test_square_str_arg(self):
        with self.assertRaises(TypeError):
            square1 = Square("1")

    def test_square_str_args(self):
        with self.assertRaises(TypeError):
            square1 = Square(1, "2")

    def test_square_str_three_args(self):
        with self.assertRaises(TypeError):
            square1 = Square(1, 2, "3")

    def test_square_neg(self):
        with self.assertRaises(ValueError):
            square1 = Square(-1)

    def test_neg_args(self):
        with self.assertRaises(ValueError):
            square1 = Square(1, -2)

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            square1 = Square(1, 2, -3)

    def test_zero(self):
        with self.assertRaises(ValueError):
            square1 = Square(0)

    def test_str_method(self):
        square1 = Square(4, 2, 3, 11)
        self.assertEqual("[Square] (11) 2/3 - 4", square1.__str__())

    def test_update(self):
        square1 = Square(4, 2, 3, 11)
        square1.update(12)
        self.assertEqual(12, square1.id)

    def test_update_two_args(self):
        square1 = Square(4, 2, 3, 11)
        square1.update(12, 1)
        self.assertEqual(12, square1.id)
        self.assertEqual(1, square1.size)

    def test_update_three_args(self):
        square1 = Square(4, 2, 3, 11)
        square1.update(12, 1, 3)
        self.assertEqual(12, square1.id)
        self.assertEqual(1, square1.size)
        self.assertEqual(3, square1.x)

    def test_update_four_args(self):
        square1 = Square(4, 2, 3, 11)
        square1.update(12, 1, 3, 4)
        self.assertEqual(12, square1.id)
        self.assertEqual(1, square1.size)
        self.assertEqual(3, square1.x)
        self.assertEqual(4, square1.y)

    def test_to_dict(self):
        square1 = Square(4, 2, 3, 11)
        dict1 = {
                "size": 4,
                "x": 2,
                "y": 3,
                "id": 11
                }
        self.assertEqual(dict1, square1.to_dictionary())

    def test_create_dict(self):
        dict1 = {
                "size": 4,
                "x": 2,
                "y": 3,
                "id": 11
                }
        square1 = Square.create(**dict1)

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r", encoding="utf-8") as f:
            string = f.read()
            self.assertEqual(str, type(string))

    def test_save_to_empty_file(self):
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        square1 = Square(4, 2, 3, 11)
        Square.save_to_file([square1])
        sqlist = Square.load_from_file()
        self.assertEqual(str(square1), str(sqlist[0]))
