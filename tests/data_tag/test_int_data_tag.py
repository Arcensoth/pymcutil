import unittest

from pymcutil.constants import INT_MIN, INT_MAX
from pymcutil.data_tag.int_data_tag import IntDataTag


class IntDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = IntDataTag()
        self.assertEqual(dt.value, 0)
        self.assertEqual(dt.to_str(), '0')

    def test_positive(self):
        dt = IntDataTag(123_456_789)
        self.assertEqual(dt.value, 123_456_789)
        self.assertEqual(dt.to_str(), '123456789')

    def test_negative(self):
        dt = IntDataTag(-123_456_789)
        self.assertEqual(dt.value, -123_456_789)
        self.assertEqual(dt.to_str(), '-123456789')

    def test_float_conversion(self):
        dt = IntDataTag(123_456_789.5)
        self.assertEqual(dt.value, 123_456_789)
        self.assertEqual(dt.to_str(), '123456789')

    def test_min(self):
        dt = IntDataTag(INT_MIN)
        self.assertEqual(dt.value, INT_MIN)
        self.assertEqual(dt.to_str(), f'{INT_MIN}')

    def test_max(self):
        dt = IntDataTag(INT_MAX)
        self.assertEqual(dt.value, INT_MAX)
        self.assertEqual(dt.to_str(), f'{INT_MAX}')

    def test_too_low(self):
        with self.assertRaises(ValueError):
            IntDataTag(INT_MIN - 1)

    def test_too_high(self):
        with self.assertRaises(ValueError):
            IntDataTag(INT_MAX + 1)

    def test_equality(self):
        dt1 = IntDataTag(123_456_789)
        dt2 = IntDataTag(123_456_789)
        self.assertEqual(dt1, dt2)
