#!/usr/bin/env python3

from unittest import TestCase
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


class TestCars(TestCase):

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_elec_remaining_range(self):
        e = ElectricCar(24.0, 450.0)
        e.drive(225.0)
        self.assertAlmostEqual(225.0, e.get_remaining_range(), delta=0.001)

    def test_elec_drive(self):
        e = ElectricCar(30.0, 450.0)
        e.drive(90.0)
        self.assertAlmostEqual(24.0, e.get_battery_status()[0], delta=0.001)

    def test_hyb_remaining_range(self):
        h = HybridCar(70.0, 1.5, 18.0, 220.0)
        self.assertAlmostEqual(4886.666666666, h.get_remaining_range(), delta=0.001)

    def test_hyb_run(self):
        h = HybridCar(70.0, 1.5, 18.0, 220.0)
        h.drive(230.0)
        self.assertAlmostEqual(0.0, h.get_battery_status()[0], delta=0.001)
        self.assertAlmostEqual(69.85, h.get_gas_tank_status()[0], delta=0.001)

    def test_hyb_run_two(self):
        h = HybridCar(70.0, 10.0, 18.0, 220.0)
        h.switch_to_combustion()
        h.drive(900.0)
        self.assertAlmostEqual(0.0, h.get_gas_tank_status()[0], delta=0.001)
        self.assertAlmostEqual(1.6363636363, h.get_battery_status()[0], delta=0.001)

    def test_wrongs(self):
        with self.assertRaises(Warning):
            HybridCar(4, 1.2, 20.0, 300.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, 1, 40.0, 240.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, 1.2, 30, 300.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, 1.2, 30.0, 400)
        with self.assertRaises(Warning):
            HybridCar("kek", 5.0, 4.0, 300.0)
        with self.assertRaises(Warning):
            HybridCar(-4.0, 1.2, 30.0, 300.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, -1.2, 30.0, 300.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, 1.2, -30.0, 300.0)
        with self.assertRaises(Warning):
            HybridCar(4.0, 1.2, 30.0, -300.0)
        with self.assertRaises(Warning):
            ElectricCar(4, 6.0)
        with self.assertRaises(Warning):
            ElectricCar(4.0, '6.0')
        with self.assertRaises(Warning):
            ElectricCar(-5.0, 6.0)
        with self.assertRaises(Warning):
            ElectricCar(4.0, -6.0)
        with self.assertRaises(Warning):
            CombustionCar('d', 6.0)
        with self.assertRaises(Warning):
            CombustionCar(5.0, 6)
        with self.assertRaises(Warning):
            CombustionCar(-45.0, 6.0)
        with self.assertRaises(Warning):
            CombustionCar(50.0, -9.0)
        e = ElectricCar(30.0, 450.0)
        with self.assertRaises(Warning):
            e.drive(5)
        with self.assertRaises(Warning):
            e.drive(-9.0)
        with self.assertRaises(Warning):
            e.charge('d')
        with self.assertRaises(Warning):
            e.charge(-2)
        with self.assertRaises(Warning):
            e.drive(500.0)
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive('c')
        with self.assertRaises(Warning):
            c.drive(-9.0)
        with self.assertRaises(Warning):
            c.fuel("kek")
        with self.assertRaises(Warning):
            c.fuel(-2)
        with self.assertRaises(Warning):
            c.drive(690.0)
        h = HybridCar(70.0, 20.0, 18.0, 220.0)
        with self.assertRaises(Warning):
            h.drive(6900.0)
        k = HybridCar(70.0, 20.0, 18.0, 220.0)
        with self.assertRaises(Warning):
            k.drive('kek')
        with self.assertRaises(Warning):
            k.drive(-9)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
