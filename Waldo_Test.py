import unittest
from Where_Waldo import where_is_waldo


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        list = []
        actual = where_is_waldo(list)
        expected = None
        self.assertEqual(actual, expected)  # add assertion here

    def test_index(self):
        list = ["bruh", "these", "Waldo", "NUTS"]
        actual = where_is_waldo(list)
        expected = 2
        self.assertEqual(actual, expected)

    def test_no_Waldo(self):
        list = ["bruh", "these", "NUTS"]
        actual = where_is_waldo(list)
        expected = None
        self.assertEqual(actual, expected)

    def test_more_Waldo(self):
        list = ["Waldo", "Bruh", "Yeet", "Waldo", "these"]
        actual = where_is_waldo(list)
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
