import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.double_data_tag import DoubleDataTag
from pymcutil.data_tag.helper import data_taggify
from pymcutil.data_tag.int_data_tag import IntDataTag
from pymcutil.data_tag.list_data_tag import ListDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class ByteDataTagTestCase(unittest.TestCase):
    def test_convert_data_tag(self):
        dt1 = data_taggify('hello')
        dt2 = data_taggify(dt1)
        self.assertEqual(dt1, dt2)

    def test_convert_bool(self):
        self.assertEqual(data_taggify(True), ByteDataTag(True))

    def test_convert_int(self):
        self.assertEqual(data_taggify(123456789), IntDataTag(123456789))

    def test_convert_double(self):
        self.assertEqual(data_taggify(123.5), DoubleDataTag(123.5))

    def test_convert_str(self):
        self.assertEqual(data_taggify('hello'), StringDataTag('hello'))

    def test_convert_list(self):
        self.assertEqual(data_taggify([]), ListDataTag([]))

    def test_convert_dict(self):
        self.assertEqual(data_taggify({}), CompoundDataTag({}))

    def test_unconvertible(self):
        with self.assertRaises(TypeError):
            data_taggify(None)
