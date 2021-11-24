#!/usr/bin/env python3

from unittest import TestCase
from cube import Cube
from cone import Cone
from cylinder import Cylinder


class CubeTest(TestCase):

    # Test if the getter for color works properly
    def test_cube_get_color(self):
        cube = Cube(10, "red", True)
        actual = cube.get_color()
        self.assertEqual(actual, "red")
        area = cube.get_area()
        self.assertEqual(600.00, area)
        self.assertIsInstance(area, float)
        volume = cube.get_volume()
        self.assertEqual(1000.00, volume)
        self.assertIsInstance(volume, float)
        length = cube.get_side_length()
        self.assertEqual(10.0, length)
        self.assertIsInstance(length, float)
        filled = cube.get_filled()
        self.assertEqual(True, filled)

    def test_cone_get_color(self):
        cone = Cone(10, 5, 6.4, "yellow", False)
        actual = cone.get_color()
        self.assertEqual(actual, "yellow")
        area = cone.get_area()
        self.assertEqual(514.96, area)
        self.assertIsInstance(area, float)
        volume = cone.get_volume()
        self.assertEqual(523.33, volume)
        self.assertIsInstance(volume, float)
        filled = cone.get_filled()
        self.assertEqual(False, filled)

    def test_cylinder_get_color(self):
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_color()
        self.assertEqual(actual, "blue")
        area = cylinder.get_area()
        self.assertEqual(176.94, area)
        self.assertIsInstance(area, float)
        volume = cylinder.get_volume()
        self.assertEqual(242.33, volume)
        self.assertIsInstance(volume, float)
        filled = cylinder.get_filled()
        self.assertEqual(True, filled)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
