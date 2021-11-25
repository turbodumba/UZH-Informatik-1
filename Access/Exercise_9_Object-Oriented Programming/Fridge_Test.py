#!/usr/bin/env python3
from unittest import TestCase
from Fridge import Fridge


class PublicTestSuite(TestCase):

    def test_example(self):
        f = Fridge()
        # put an item into the fridge
        f.store((191112, "Butter"))
        self.assertEqual(1, len(f))
        # take it out again
        item = f.take((191112, "Butter"))
        self.assertEqual(0, len(f))
        # is it the right item?
        self.assertEqual((191112, "Butter"), item)

    def test_two(self):
        f = Fridge()
        f.store((211129, "Milk"))
        f.store((211128, "Butter"))
        f.store((211124, "Chicken"))
        f.store((211208, "Cream"))
        f.store((211128, "Butter"))
        f.store((211129, "Butter"))
        f.store((211224, "Pesto"))
        self.assertEqual(7, len(f))
        item = f.take((211128, "Butter"))
        self.assertEqual((211128, "Butter"), item)
        list = f.take_before(211129)
        expected = [(211124, "Chicken"), (211128, "Butter")]
        self.assertEqual(expected, list)
        list = f.take_before(211129)
        expected = []
        self.assertEqual(expected, list)
        self.assertEqual(4, len(f))

    def test_None(self):
        f = Fridge()
        f.store((220101, "Bread"))
        actual = f.find((220102, "Bread"))
        self.assertEqual(None, actual)

    def test_Warning(self):
        f = Fridge()
        f.store((211224, "Milk"))
        with self.assertRaises(Warning):
            f.take((211223, "Milk"))

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
