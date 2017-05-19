import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.float_data_tag import FloatDataTag
from pymcutil.data_tag.helper import data_taggify
from pymcutil.data_tag.int_data_tag import IntDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class ByteDataTagTestCase(unittest.TestCase):
    def test_convert_data_tag(self):
        dt1 = data_taggify('hello')
        dt2 = data_taggify(dt1)
        self.assertEqual(dt1, dt2)

    def test_convert_dict(self):
        dt = data_taggify({})
        self.assertEqual(dt, CompoundDataTag({}))

    def test_convert_bool(self):
        dt = data_taggify(True)
        self.assertEqual(dt, ByteDataTag(True))

    def test_convert_int(self):
        dt = data_taggify(123456789)
        self.assertEqual(dt, IntDataTag(123456789))

    def test_convert_float(self):
        dt = data_taggify(123.5)
        self.assertEqual(dt, FloatDataTag(123.5))

    def test_convert_str(self):
        dt = data_taggify('hello')
        self.assertEqual(dt, StringDataTag('hello'))

    def test_unconvertible(self):
        with self.assertRaises(TypeError):
            data_taggify(None)
