#!/usr/bin/env python3
from unittest import TestCase
from Fine_Calc import fine_calculator


# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class FineCalculatorTest(TestCase):

    def test_wrong_area_type(self):
        actual = fine_calculator(3, 15)
        expected = "Invalid Area Type"
        self.assertEqual(actual, expected)

    def test_wrong_area_value_one(self):
        actual = fine_calculator("Motorway", 150)
        expected = "Invalid Area Value"
        self.assertEqual(actual, expected)

    def test_wrong_area_value_two(self):
        actual = fine_calculator("Urban", 78)
        expected = "Invalid Area Value"
        self.assertEqual(actual, expected)

    def test_wrong_area_value_three(self):
        actual = fine_calculator("Expressway", 115)
        expected = "Invalid Area Value"
        self.assertEqual(actual, expected)

    def test_wrong_speed_type(self):
        actual = fine_calculator("urban", "bruh")
        expected = "Invalid Speed Type"
        self.assertEqual(actual, expected)

    def test_wrong_speed_value(self):
        actual = fine_calculator("urban", -69)
        expected = "Invalid Speed Value"
        self.assertEqual(actual, expected)

    def test_zero_fine_one(self):
        actual = fine_calculator("urban", 49)
        expected = 0
        self.assertEqual(actual, expected)

    def test_zero_fine_two(self):
        actual = fine_calculator("expressway", 98)
        expected = 0
        self.assertEqual(actual, expected)

    def test_zero_fine_three(self):
        actual = fine_calculator("motorway", 115)
        expected = 0
        self.assertEqual(actual, expected)

    def test_actual_fine_one(self):
        actual = fine_calculator("motorway", 150)
        expected = 312
        self.assertEqual(actual, expected)

    def test_actual_fine_two(self):
        actual = fine_calculator("urban", 80)
        expected = 3600
        self.assertEqual(actual, expected)

    def test_actual_fine_three(self):
        actual = fine_calculator("expressway", 118)
        expected = 259
        self.assertEqual(actual, expected)

    def test_actual_fine_four(self):
        actual = fine_calculator("motorway", 280)
        expected = 8889
        self.assertEqual(actual, expected)

    def test_sample_fine(self):
        actual = fine_calculator("motorway", 180)
        expected = 1250
        self.assertEqual(actual, expected)
