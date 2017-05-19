import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.double_data_tag import DoubleDataTag
from pymcutil.data_tag.float_data_tag import FloatDataTag
from pymcutil.data_tag.int_data_tag import IntDataTag
from pymcutil.data_tag.list_data_tag import ListDataTag
from pymcutil.data_tag.long_data_tag import LongDataTag
from pymcutil.data_tag.short_data_tag import ShortDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class CompoundDataTagTestCase(unittest.TestCase):
    def test_everything(self):
        dt = CompoundDataTag(
            explicitbyte=ByteDataTag(True),
            explicitshort=ShortDataTag(12),
            explicitint=IntDataTag(123),
            explicitlong=LongDataTag(1234),
            explicitfloat=FloatDataTag(1234.5),
            explicitdouble=DoubleDataTag(1234.56),
            explicitstring=StringDataTag('hello'),
            explicitlist=ListDataTag([False, 9001, 'item']),
            explicitcompound=CompoundDataTag({'key1': True, 'key2': 25565, 'key3': 'stringvalue'}),
            anotherexplicitcompound=CompoundDataTag(key4=False, key5=25566, key6='stringvalue2'),
            implicitbyte=False,
            implicitint=321,
            implicitdouble=6543.21,
            implicitstring='goodbye',
            implicitlist=[True, 9002, 'anotheritem'],
            implicitcompound={'key7': True, 'key8': 25567, 'key9': 'stringvalue3'},
            anotherimplicitcompound=dict(key10=False, key11=25568, key12='stringvalue4'),
            breakingstring='breaking:string',
            quotedstring='quoted"string',
            innerbreakingstring=['inner:breakingstring'],
            innerquotedstring=['inner"quotedstring'],
            deepbreakingstring=[dict(one=[dict(two=[dict(three='deep:breakingstring')])])],
            deepquotedstring=[dict(one=[dict(two=[dict(three='deep"quotedstring')])])])
        self.assertEqual(
            dt.to_str(),
            r"""
{explicitbyte:1b,explicitshort:12s,explicitint:123,explicitlong:1234l,explicitfloat:1234.5f,explicitdouble:1234.56d,
explicitstring:hello,explicitlist:[0b,9001,item],explicitcompound:{key1:1b,key2:25565,key3:stringvalue},
anotherexplicitcompound:{key4:0b,key5:25566,key6:stringvalue2},implicitbyte:0b,implicitint:321,implicitdouble:6543.21d,
implicitstring:goodbye,implicitlist:[1b,9002,anotheritem],implicitcompound:{key7:1b,key8:25567,key9:stringvalue3},
anotherimplicitcompound:{key10:0b,key11:25568,key12:stringvalue4},breakingstring:"breaking:string",
quotedstring:"quoted\"string",innerbreakingstring:["inner:breakingstring"],innerquotedstring:["inner\"quotedstring"],
deepbreakingstring:[{one:[{two:[{three:"deep:breakingstring"}]}]}],
deepquotedstring:[{one:[{two:[{three:"deep\"quotedstring"}]}]}]}
""".replace('\n', ''))
