#!/usr/bin/env python3
""" unit test """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ testcase """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)

        self.assertEqual(str(error.exception.args[0]), path[-1] )

class TestGetJson(unittest.TestCase):
    """ test json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ TESTCASE """
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
            returned but a_method is only called once using assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once

if __name__ == "__main__":
    unittest.main()
