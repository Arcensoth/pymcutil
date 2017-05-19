import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.double_data_tag import DoubleDataTag
from pymcutil.data_tag.float_data_tag import FloatDataTag
from pymcutil.data_tag.int_data_tag import IntDataTag
from pymcutil.data_tag.long_data_tag import LongDataTag
from pymcutil.data_tag.short_data_tag import ShortDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class CompoundDataTagTestCase(unittest.TestCase):
    def test_get(self):
        dt = CompoundDataTag(mykey='myvalue')
        self.assertEqual(dt['mykey'], StringDataTag('myvalue'))

    def test_set(self):
        dt = CompoundDataTag()
        dt['mykey'] = 'myvalue'
        self.assertEqual(dt['mykey'], StringDataTag('myvalue'))

    def test_overwrite(self):
        dt = CompoundDataTag(mykey='myvalue')
        dt['mykey'] = 'anothervalue'
        self.assertEqual(dt['mykey'], StringDataTag('anothervalue'))

    def test_del_only(self):
        dt = CompoundDataTag(mykey='myvalue')
        self.assertEqual(dt.to_str(), '{mykey:myvalue}')
        del dt['mykey']
        self.assertEqual(dt.to_str(), '{}')

    def test_del_with_remaining(self):
        dt = CompoundDataTag(mykey='myvalue', anotherkey='anothervalue')
        self.assertEqual(dt.to_str(), '{mykey:myvalue,anotherkey:anothervalue}')
        del dt['mykey']
        self.assertEqual(dt.to_str(), '{anotherkey:anothervalue}')

    def test_default(self):
        dt = CompoundDataTag()
        self.assertEqual(dt.to_str(), '{}')

    def test_empty_dict(self):
        dt = CompoundDataTag({})
        self.assertEqual(dt.to_str(), '{}')

    def test_multi_empty_dicts(self):
        dt = CompoundDataTag({}, {})
        self.assertEqual(dt.to_str(), '{}')

    def test_nonempty_dict_and_kwargs(self):
        dt = CompoundDataTag({'mykey': 'myvalue'}, anotherkey='anothervalue')
        self.assertEqual(dt.to_str(), '{mykey:myvalue,anotherkey:anothervalue}')

    def test_nonempty_dict_and_kwargs_overwriting(self):
        dt = CompoundDataTag({'mykey': 'myvalue'}, mykey='anothervalue')
        self.assertEqual(dt.to_str(), '{mykey:anothervalue}')

    def test_key_and_value(self):
        dt = CompoundDataTag(mykey='myvalue')
        self.assertEqual(dt.to_str(), '{mykey:myvalue}')

    def test_breaking_key_and_value(self):
        dt = CompoundDataTag({'my:key': 'somevalue'})
        self.assertEqual(dt.to_str(), '{"my:key":somevalue}')

    def test_key_and_breaking_value(self):
        dt = CompoundDataTag({'mykey': 'some:value'})
        self.assertEqual(dt.to_str(), '{mykey:"some:value"}')

    def test_breaking_key_and_breaking_value(self):
        dt = CompoundDataTag({'my:key': 'some:value'})
        self.assertEqual(dt.to_str(), '{"my:key":"some:value"}')

    def test_empty_value(self):
        dt = CompoundDataTag(mykey='')
        self.assertEqual(dt.to_str(), '{mykey:""}')

    def test_questionable_keys(self):
        dt = CompoundDataTag({'ke_y': 'value1', 'k.e--+_y': 'value2'})
        self.assertEqual(dt.to_str(), '{ke_y:value1,k.e--+_y:value2}')

    def test_questionable_values(self):
        dt = CompoundDataTag(key1='v__alue', key2='v.-_+alue')
        self.assertEqual(dt.to_str(), '{key1:v__alue,key2:v.-_+alue}')

    def test_breaking_keys(self):
        dt = CompoundDataTag({'ke$y': 'value1', 'ke y': 'value2', 'ke:y': 'value3'})
        self.assertEqual(dt.to_str(), '{"ke$y":value1,"ke y":value2,"ke:y":value3}')

    def test_breaking_values(self):
        dt = CompoundDataTag(key1='va lue', key2='va$lue', key3='minecraft:stone')
        self.assertEqual(dt.to_str(), '{key1:"va lue",key2:"va$lue",key3:"minecraft:stone"}')

    def test_key_with_quotes(self):
        dt = CompoundDataTag({'my"key': 'myvalue'})
        self.assertEqual(dt.to_str(), r'{"my\"key":myvalue}')

    def test_value_with_quotes(self):
        dt = CompoundDataTag(mykey='my"value')
        self.assertEqual(dt.to_str(), r'{mykey:"my\"value"}')

    def test_byte_data_tag_conversion(self):
        dt = CompoundDataTag(mybyte=ByteDataTag(True))
        self.assertEqual(dt.to_str(), '{mybyte:1b}')

    def test_short_data_tag_conversion(self):
        dt = CompoundDataTag(myshort=ShortDataTag(1234))
        self.assertEqual(dt.to_str(), '{myshort:1234s}')

    def test_int_data_tag_conversion(self):
        dt = CompoundDataTag(myint=IntDataTag(123456789))
        self.assertEqual(dt.to_str(), '{myint:123456789}')

    def test_long_data_tag_conversion(self):
        dt = CompoundDataTag(mylong=LongDataTag(111222333444555))
        self.assertEqual(dt.to_str(), '{mylong:111222333444555l}')

    def test_float_data_tag_conversion(self):
        dt = CompoundDataTag(myfloat=FloatDataTag(123.5))
        self.assertEqual(dt.to_str(), '{myfloat:123.5f}')

    def test_double_data_tag_conversion(self):
        dt = CompoundDataTag(mydouble=DoubleDataTag(456.5))
        self.assertEqual(dt.to_str(), '{mydouble:456.5d}')

    def test_string_data_tag_conversion(self):
        dt = CompoundDataTag(mystring=StringDataTag('hello'))
        self.assertEqual(dt.to_str(), '{mystring:hello}')

    def test_compound_data_tag_conversion(self):
        dt = CompoundDataTag(inner=CompoundDataTag(innerkey='innervalue'))
        self.assertEqual(dt.to_str(), '{inner:{innerkey:innervalue}}')

    def test_deep_compound_data_tag_conversion(self):
        dt = CompoundDataTag(one=dict(two={'three': dict(four='five')}))
        self.assertEqual(dt.to_str(), '{one:{two:{three:{four:five}}}}')

    def test_everything(self):
        dt = CompoundDataTag(
            mystring='somestring',
            mybyte=True,
            myemptycompound={},
            mycompound=dict(
                myinnerstring='someinnerstring',
                myinnerbyte=False,
                myinneremptycompound={}))
        self.assertEqual(
            dt.to_str(),
            '{mystring:somestring,mybyte:1b,myemptycompound:{},mycompound:'
            '{myinnerstring:someinnerstring,myinnerbyte:0b,myinneremptycompound:{}}'
            '}')
