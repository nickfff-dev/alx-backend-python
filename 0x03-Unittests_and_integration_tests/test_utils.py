#!/usr/bin/env python3
"""Generic utilities for github org client."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function in utils."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected results."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError with the expected
        message for invalid inputs."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertIn(path[-1], str(context.exception))


class TestGetJson(unittest.TestCase):
    """Test class for the get_json function in utils."""
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected results."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
        mock_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
