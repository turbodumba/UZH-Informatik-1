#!/usr/bin/env python3

from unittest import TestCase
from word_logic import WordLogic
from number_logic import NumberLogic


class PublicTestSuite(TestCase):

    def test_example(self):
        w = WordLogic(10, 7, 5)
        self.assertEqual(10, w.num_words)
        self.assertEqual(7, w.len_words)
        self.assertEqual(5, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)

    def test_num_logic(self):
        n = NumberLogic(10, 7, 5)
        self.assertEqual(10, n.num_words)
        self.assertEqual(7, n.len_words)
        self.assertEqual(5, n.num_attempts)
        self.assertEqual(len(n.words), n.num_words)
        self.assertEqual(n.password in n.words, True)
        with self.assertRaises(Warning):
            n.check('3458')
        with self.assertRaises(Warning):
            n.check('8729690')

        l = NumberLogic(10,3,2)
        print('Password: ' + l.password)
        print(l.check('286'))
        print(l.check('942'))
        with self.assertRaises(Warning):
            print(l.check('000'))



    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
