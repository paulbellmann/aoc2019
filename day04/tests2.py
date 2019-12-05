import unittest
from part02 import *


class MyTest(unittest.TestCase):

    def test_is_six_digit_rule(self):
        self.assertEqual(is_six_digit_rule(123456), True)
        self.assertEqual(is_six_digit_rule(12345), False)

    def test_is_in_given_range(self):
        self.assertEqual(is_in_given_range(10, 20, 15), True)
        self.assertEqual(is_in_given_range(10, 20, 20), True)
        self.assertEqual(is_in_given_range(10, 20, 10), True)
        self.assertEqual(is_in_given_range(10, 20, 21), False)
        self.assertEqual(is_in_given_range(10, 20, 9), False)

    def test_is_not_decreasing(self):
        self.assertEqual(is_not_decreasing(123), True)
        self.assertEqual(is_not_decreasing(12334), True)
        self.assertEqual(is_not_decreasing(12332), False)

    def test_has_two_adjacent_same_digits(self):

        self.assertEqual(has_two_adjacent_same_digits(12333), False)
        self.assertEqual(has_two_adjacent_same_digits(123333), True)
        self.assertEqual(has_two_adjacent_same_digits(112233), True)
        self.assertEqual(has_two_adjacent_same_digits(123444), False)
        self.assertEqual(has_two_adjacent_same_digits(111122), True)


if __name__ == "__main__":
    unittest.main()
