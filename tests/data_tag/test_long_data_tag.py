import unittest

from pymcutil.constants import LONG_MIN, LONG_MAX
from pymcutil.data_tag.long_data_tag import LongDataTag


class LongDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = LongDataTag()
        self.assertEqual(dt.value, 0)
        self.assertEqual(dt.to_str(), '0l')

    def test_positive(self):
        dt = LongDataTag(1_234)
        self.assertEqual(dt.value, 1_234)
        self.assertEqual(dt.to_str(), '1234l')

    def test_negative(self):
        dt = LongDataTag(-1_234)
        self.assertEqual(dt.value, -1_234)
        self.assertEqual(dt.to_str(), '-1234l')

    def test_float_conversion(self):
        dt = LongDataTag(1_234.5)
        self.assertEqual(dt.value, 1_234)
        self.assertEqual(dt.to_str(), '1234l')

    def test_min(self):
        dt = LongDataTag(LONG_MIN)
        self.assertEqual(dt.value, LONG_MIN)
        self.assertEqual(dt.to_str(), f'{LONG_MIN}l')

    def test_max(self):
        dt = LongDataTag(LONG_MAX)
        self.assertEqual(dt.value, LONG_MAX)
        self.assertEqual(dt.to_str(), f'{LONG_MAX}l')

    def test_too_low(self):
        with self.assertRaises(ValueError):
            LongDataTag(LONG_MIN - 1)

    def test_too_high(self):
        with self.assertRaises(ValueError):
            LongDataTag(LONG_MAX + 1)

    def test_equality(self):
        dt1 = LongDataTag(1_234)
        dt2 = LongDataTag(1_234)
        self.assertEqual(dt1, dt2)
