import unittest

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag
from pymcutil.entity.abc.entity import Entity


class EntityTestCase(unittest.TestCase):
    def test_with_id(self):
        e = Entity('zombie')
        self.assertEqual(e.entity_id, 'zombie')

    def test_with_id_and_data_tag(self):
        e = Entity('zombie', data_tag=CompoundDataTag(custom_name='Bob'))
        self.assertEqual(e.entity_id, 'zombie')
        self.assertEqual(e.data_tag['custom_name'], StringDataTag('Bob'))

    def test_data_tag_from_dict(self):
        e = Entity('zombie', data_tag=dict(custom_name='Bob'))
        self.assertEqual(e.data_tag['custom_name'], StringDataTag('Bob'))

    def test_data_tag_from_braces(self):
        e = Entity('zombie', data_tag={'CustomName': 'Bob'})
        self.assertEqual(e.data_tag['CustomName'], StringDataTag('Bob'))

    def test_tag(self):
        e1 = Entity('zombie')
        e2 = e1.tag({'CustomName': 'Bob'})
        self.assertEqual(e1.entity_id, 'zombie')
        self.assertEqual(e1.data_tag, CompoundDataTag())
        self.assertEqual(e2.entity_id, 'zombie')
        self.assertEqual(e2.data_tag, CompoundDataTag({'CustomName': 'Bob'}))

    def test_tag_overwrite(self):
        e1 = Entity('zombie', data_tag=CompoundDataTag({'CustomName': 'Bob'}))
        e2 = e1.tag({'CustomName': 'Doug'})
        self.assertEqual(e1.entity_id, 'zombie')
        self.assertEqual(e1.data_tag, CompoundDataTag({'CustomName': 'Bob'}))
        self.assertEqual(e2.entity_id, 'zombie')
        self.assertEqual(e2.data_tag, CompoundDataTag({'CustomName': 'Doug'}))

    def test_tag_more(self):
        e1 = Entity('zombie', data_tag=CompoundDataTag({'CustomName': 'Bob'}))
        e2 = e1.tag({'NoAI': True})
        self.assertEqual(e1.entity_id, 'zombie')
        self.assertEqual(e1.data_tag, CompoundDataTag({'CustomName': 'Bob'}))
        self.assertEqual(e2.entity_id, 'zombie')
        self.assertEqual(e2.data_tag, CompoundDataTag({'CustomName': 'Bob', 'NoAI': True}))

