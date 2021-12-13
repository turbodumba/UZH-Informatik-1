#!/usr/bin/env python3
from unittest import TestCase
from currency_converter import convert
from bank_account import BankAccount


# You need to add missing imports to make the test work!

class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        with self.assertRaises(Warning):
            convert('k', 'EUR', 'CHF')
        with self.assertRaises(Warning):
            convert(3, 'CHF', 'CNY')
        with self.assertRaises(Warning):
            convert(6.9, 'CNY', 'CHF')
        actual = convert(5.0, 'CHF', 'EUR')
        expected = 4.545454545454546
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        with self.assertRaises(Warning):
            convert(5.0, '', 'CHF')

    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_2_curr_not_available(self):
        with self.assertRaises(Warning):
            sut = BankAccount("CNY")

    def test_3_curr_balance(self):
        kek = BankAccount('CHF')
        with self.assertRaises(Warning):
            kek.deposit(-5)
        with self.assertRaises(Warning):
            kek.withdraw(-5)
        kek.deposit(500)
        with self.assertRaises(Warning):
            kek.withdraw(690)
        with self.assertRaises(Warning):
            kek.withdraw(20, 'CNY')
        with self.assertRaises(Warning):
            kek.deposit(30, 'CNY')

    def test_4_not_mentioned(self):
        lul = BankAccount('USD')
        with self.assertRaises(Warning):
            lul.deposit('kek', 'EUR')
        with self.assertRaises(Warning):
            lul.withdraw('bruh', 'JPY')

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
