import unittest
import os
from solution import sum_two


class TestStrictDecorator(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(0, 0), 0)
        self.assertEqual(sum_two(-1, 1), 0)

    def test_invalid_argument_count(self):
        with self.assertRaises(TypeError):
            sum_two(1)
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)

    def test_invalid_argument_type(self):
        with self.assertRaises(TypeError):
            sum_two(1, '2')
        with self.assertRaises(TypeError):
            sum_two(1.0, 2)
        with self.assertRaises(TypeError):
            sum_two(1, None)
