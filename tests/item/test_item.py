import unittest

from pymcutil.data_tag.byte_data_tag import ByteDataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.item.item import Item


class ItemTestCase(unittest.TestCase):
    def test_with_id(self):
        i = Item('diamond')
        self.assertEqual(i.item_id, 'diamond')

    def test_with_id_and_data_tag(self):
        i = Item('diamond', data_tag=CompoundDataTag(count=ByteDataTag(64)))
        self.assertEqual(i.item_id, 'diamond')
        self.assertEqual(i.data_tag['count'], ByteDataTag(64))

    def test_data_tag_from_dict(self):
        i = Item('diamond', data_tag=dict(count=ByteDataTag(64)))
        self.assertEqual(i.data_tag['count'], ByteDataTag(64))

    def test_data_tag_from_braces(self):
        i = Item('diamond', data_tag={'Count': ByteDataTag(64)})
        self.assertEqual(i.data_tag['Count'], ByteDataTag(64))

    def test_tag(self):
        i1 = Item('diamond')
        i2 = i1.tag({'Count': ByteDataTag(64)})
        self.assertEqual(i1.item_id, 'diamond')
        self.assertEqual(i1.data_tag, CompoundDataTag())
        self.assertEqual(i2.item_id, 'diamond')
        self.assertEqual(i2.data_tag, CompoundDataTag({'Count': ByteDataTag(64)}))

    def test_tag_overwrite(self):
        i1 = Item('diamond', data_tag=CompoundDataTag({'Count': ByteDataTag(64)}))
        i2 = i1.tag({'Count': ByteDataTag(32)})
        self.assertEqual(i1.item_id, 'diamond')
        self.assertEqual(i1.data_tag, CompoundDataTag({'Count': ByteDataTag(64)}))
        self.assertEqual(i2.item_id, 'diamond')
        self.assertEqual(i2.data_tag, CompoundDataTag({'Count': ByteDataTag(32)}))

    def test_tag_more(self):
        i1 = Item('diamond', data_tag=CompoundDataTag({'Count': ByteDataTag(64)}))
        i2 = i1.tag({'Slot': ByteDataTag(8)})
        self.assertEqual(i1.item_id, 'diamond')
        self.assertEqual(i1.data_tag, CompoundDataTag({'Count': ByteDataTag(64)}))
        self.assertEqual(i2.item_id, 'diamond')
        self.assertEqual(i2.data_tag, CompoundDataTag({'Count': ByteDataTag(64), 'Slot': ByteDataTag(8)}))
