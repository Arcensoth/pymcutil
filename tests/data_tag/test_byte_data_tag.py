import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag


class ByteDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = ByteDataTag()
        self.assertEqual(dt.value, 0)
        self.assertEqual(dt.to_str(), '0b')

    def test_positive(self):
        dt = ByteDataTag(1)
        self.assertEqual(dt.value, 1)
        self.assertEqual(dt.to_str(), '1b')

    def test_negative(self):
        dt = ByteDataTag(-1)
        self.assertEqual(dt.value, -1)
        self.assertEqual(dt.to_str(), '-1b')

    def test_float_conversion(self):
        dt = ByteDataTag(1.5)
        self.assertEqual(dt.value, 1)
        self.assertEqual(dt.to_str(), '1b')

    def test_too_low(self):
        with self.assertRaises(ValueError):
            ByteDataTag(-129)

    def test_too_high(self):
        with self.assertRaises(ValueError):
            ByteDataTag(128)

    def test_equality(self):
        dt1 = ByteDataTag(1)
        dt2 = ByteDataTag(1)
        self.assertEqual(dt1, dt2)
