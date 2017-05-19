import unittest

from pymcutil.constants import SHORT_MIN, SHORT_MAX
from pymcutil.data_tag.short_data_tag import ShortDataTag


class ShortDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = ShortDataTag()
        self.assertEqual(dt.value, 0)
        self.assertEqual(dt.to_str(), '0s')

    def test_positive(self):
        dt = ShortDataTag(1_234)
        self.assertEqual(dt.value, 1_234)
        self.assertEqual(dt.to_str(), '1234s')

    def test_negative(self):
        dt = ShortDataTag(-1_234)
        self.assertEqual(dt.value, -1_234)
        self.assertEqual(dt.to_str(), '-1234s')

    def test_float_conversion(self):
        dt = ShortDataTag(1_234.5)
        self.assertEqual(dt.value, 1_234)
        self.assertEqual(dt.to_str(), '1234s')

    def test_min(self):
        dt = ShortDataTag(SHORT_MIN)
        self.assertEqual(dt.value, SHORT_MIN)
        self.assertEqual(dt.to_str(), f'{SHORT_MIN}s')

    def test_max(self):
        dt = ShortDataTag(SHORT_MAX)
        self.assertEqual(dt.value, SHORT_MAX)
        self.assertEqual(dt.to_str(), f'{SHORT_MAX}s')

    def test_too_low(self):
        with self.assertRaises(ValueError):
            ShortDataTag(SHORT_MIN - 1)

    def test_too_high(self):
        with self.assertRaises(ValueError):
            ShortDataTag(SHORT_MAX + 1)

    def test_equality(self):
        dt1 = ShortDataTag(1_234)
        dt2 = ShortDataTag(1_234)
        self.assertEqual(dt1, dt2)
