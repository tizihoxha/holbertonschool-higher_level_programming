#!/usr/bin/python3
import unittest
from models.base import Base
"""Tests"""


class BaseTest(unittest.TestCase):
    """Test class"""
    def test_id_none(self):
        """id is none"""
        inst = Base()
        self.assertEqual(1, inst.id)

    def test_id(self):
        """test id"""
        inst = Base(15)
        self.assertEqual(15, inst.id)

    def test_negative_id(self):
        """negative id"""
        inst = Base(-4)
        self.assertEqual(-4, inst.id)

    def test_zero_id(self):
        inst = Base(0)
        self.assertEqual(0, inst.id)

    def test_id_is_string(self):
        inst = Base("Hello")
        self.assertEqual("Hello", inst.id)

    def test_id_is_list(self):
        inst = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], inst.id)

    def test_id_is_tuple(self):
        inst = Base((1, ))
        self.assertEqual((1, ), inst.id)

    def test_to_json(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])
