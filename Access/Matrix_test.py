#!/usr/bin/env python3

from unittest import TestCase
from Matrix import Matrix


class PublicTestSuite(TestCase):

    def assertFailedInit(self, A):
        with self.assertRaises(AssertionError) as ctx:
            A = Matrix(A)

    def test0_empty_list(self):
        self.assertFailedInit([])

    def test1_wrong_input(self):
        self.assertFailedInit("sdf")

    def test2_wrong_input(self):
        self.assertFailedInit(["sdf"])

    def test3_wrong_input(self):
        self.assertFailedInit([[]])

    def test4_wrong_input(self):
        self.assertFailedInit([["dd"]])

    def test5_wrong_input(self):
        self.assertFailedInit([1, 2, 3])

    def test6_wrong_input(self):
        self.assertFailedInit([[3, 4, 7], [8, 9, 4], [3, 9, 0, 2], [2, 3, 4]])

    def test7_wrong_input(self):
        self.assertFailedInit([[[3, 5], 5], [3, 4], [1, 9]])

    def test8_wrong_input(self):
        self.assertFailedInit([[3, 6, 5], [8, 2, 3], 7, [0, 7, 3]])

    def test9_wrong_input(self):
        self.assertFailedInit([[1, 2], [3, 9, 8], [9, 0, 3]])

    def test10_wrong_input(self):
        self.assertFailedInit([['3', '4'], ['3', '9']])

    def test11_wrong_input(self):
        self.assertFailedInit(["bruh", [3, 6, 5, 4]])

    def test_add(self):
        M = Matrix([[6, 9, 7, 3], [3, 4, 2, 1], [5, 43, 312, 4], [52, 4, 45, 12]])
        N = Matrix([[6, 6.0, 31.5, 37.4], [23.4, 6.5, 7.8, 9.2], [34, 5, 32, 0], [0.5, 0.3, 65, 32]])
        actual = M + N
        expected = Matrix([[12, 15, 38.5, 40.4], [26.4, 10.5, 9.8, 10.2], [39, 48, 344, 4], [52.5, 4.3, 110, 44]])
        self.assertEqual(expected, actual)

    def test_add_wrong(self):
        M = Matrix([[0, 4], [3, 6]])
        N = Matrix([[0, 3, 4], [2, 3, 4], [9, 6, 3]])
        with self.assertRaises(AssertionError):
            K = M + N

    def test_mult(self):
        M = Matrix([[6, 9, 7, 3], [3, 4, 2, 1], [5, 43, 312, 4], [52, 4, 45, 12]])
        N = Matrix([[6, 6.0, 31.5, 37.4], [23.4, 6.5, 7.8, 9.2], [34, 5, 32, 0], [0.5, 0.3, 65, 32]])
        actual = M * N
        expected = Matrix([[486.1, 130.4, 678.2, 403.2], [180.1, 54.3, 254.7, 181.0], [11646.2, 1870.7, 10736.9, 710.5999999999999],
                           [1941.6, 566.6, 3889.2, 2365.6]])
        self.assertEqual(expected, actual)

    def test_mult_wrong(self):
        M = Matrix([[3, 5, 6], [3, 6, 7], [8, 6, 3], [7, 9, 3]])
        N = Matrix([[9, 7, 2], [3, 2, 1], [9, 5, 3], [9, 5, 2]])
        with self.assertRaises(AssertionError):
            K = M * N

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
