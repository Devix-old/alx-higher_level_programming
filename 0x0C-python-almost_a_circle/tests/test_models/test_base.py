#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
'''This code to test the base class'''


class TestBase(unittest.TestCase):
    '''Represente TestBase class'''

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_custom_id(self):
        b2 = Base(100)
        self.assertEqual(b2.id, 100)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_dicts(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(
            json_str,
            '[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10}]'
        )


class Testbase_from_json_string(unittest.TestCase):
    def from_json_string_none(self):
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def from_json_string_empty(self):
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])

    def from_json_string_one_key(self):
        list_output = Base.from_json_string('[{ "id": 89 }]')
        expected_output = "[<class 'list'>] [{'id': 98}]"
        self.assertEqual(list_output, expected_output)


if __name__ == "__main__":
    unittest.main()
