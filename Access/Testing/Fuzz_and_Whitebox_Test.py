#!/usr/bin/env python3
from unittest import TestCase
from FuzzTesting_and_WhiteboxTesting import calculate_factorial


class MyTests(TestCase):

    def test_normal(self):
        actual = calculate_factorial(6)
        expected = 720
        self.assertEqual(expected, actual)

    def test_normal_two(self):
        actual = calculate_factorial(8)
        expected = 40320
        self.assertEqual(expected, actual)

    def test_negative_num(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-69)

    def test_num_over_ten(self):
        with self.assertRaises(ValueError):
            calculate_factorial(13)

    def test_zero(self):
        actual = calculate_factorial(0)
        expected = 1
        self.assertEqual(expected, actual)

    def test_string_possible(self):
        actual = calculate_factorial("4")
        expected = 24
        self.assertEqual(expected, actual)

    def test_string_wrong(self):
        with self.assertRaises(TypeError):
            calculate_factorial("4Yeet")

    def test_input_None(self):
        actual = calculate_factorial(None)
        expected = None
        self.assertEqual(expected, actual)

    def test_negative_string(self):
        with self.assertRaises(ValueError):
            calculate_factorial("-8")

    def test_over_ten_string(self):
        with self.assertRaises(ValueError):
            calculate_factorial("69")

    def test_zero_string(self):
        actual = calculate_factorial("0")
        expected = 1
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            calculate_factorial(" ")

    def test_empty(self):
        with self.assertRaises(TypeError):
            calculate_factorial("")

    def test_example(self):
        with self.assertRaises(TypeError):
            calculate_factorial(".5728//")

