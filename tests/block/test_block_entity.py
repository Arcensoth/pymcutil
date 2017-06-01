import unittest

from pymcutil.block.block_entity import BlockEntity
from pymcutil.block.block_state import BlockState
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class BlockTestCase(unittest.TestCase):
    def test_with_id(self):
        be = BlockEntity('chest')
        self.assertEqual(be.block_id, 'chest')

    def test_with_id_and_block_state(self):
        be = BlockEntity('chest', BlockState(facing='north'))
        self.assertEqual(be.block_id, 'chest')
        self.assertEqual(be.block_state['facing'], 'north')

    def test_with_id_and_block_state_and_data_tag(self):
        be = BlockEntity('chest', BlockState(facing='north'), CompoundDataTag(lock='password'))
        self.assertEqual(be.block_id, 'chest')
        self.assertEqual(be.block_state['facing'], 'north')
        self.assertEqual(be.data_tag['lock'], StringDataTag('password'))

    def test_data_tag_from_dict(self):
        be = BlockEntity('chest', data_tag=dict(lock='password'))
        self.assertEqual(be.data_tag['lock'], StringDataTag('password'))

    def test_data_tag_from_braces(self):
        be = BlockEntity('chest', data_tag={'Lock': 'password'})
        self.assertEqual(be.data_tag['Lock'], StringDataTag('password'))

    def test_tag(self):
        be1 = BlockEntity('chest')
        be2 = be1.tag({'Lock': 'password'})
        self.assertEqual(be1.block_id, 'chest')
        self.assertEqual(be1.data_tag, CompoundDataTag())
        self.assertEqual(be2.block_id, 'chest')
        self.assertEqual(be2.data_tag, CompoundDataTag({'Lock': 'password'}))

    def test_tag_overwrite(self):
        be1 = BlockEntity('chest', data_tag=CompoundDataTag({'Lock': 'password'}))
        be2 = be1.tag({'Lock': 'guessme'})
        self.assertEqual(be1.block_id, 'chest')
        self.assertEqual(be1.data_tag, CompoundDataTag({'Lock': 'password'}))
        self.assertEqual(be2.block_id, 'chest')
        self.assertEqual(be2.data_tag, CompoundDataTag({'Lock': 'guessme'}))

    def test_tag_more(self):
        be1 = BlockEntity('chest', data_tag=CompoundDataTag({'Lock': 'password'}))
        be2 = be1.tag({'CustomName': 'Materials'})
        self.assertEqual(be1.block_id, 'chest')
        self.assertEqual(be1.data_tag, CompoundDataTag({'Lock': 'password'}))
        self.assertEqual(be2.block_id, 'chest')
        self.assertEqual(be2.data_tag, CompoundDataTag({'Lock': 'password', 'CustomName': 'Materials'}))
