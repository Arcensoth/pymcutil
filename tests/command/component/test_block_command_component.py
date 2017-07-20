import unittest

from pymcutil.block.block_entity import BlockEntity
from pymcutil.data_tag.compound_data_tag import CompoundDataTag

from pymcutil.block.block_state import BlockState
from pymcutil.command.component.block_command_component import BlockCommandComponent


class BlockCommandComponentTestCase(unittest.TestCase):
    def test_block_id(self):
        cc = BlockCommandComponent(block_id='dropper')
        self.assertEqual(cc.block_id, 'dropper')

    def test_missing_block_id(self):
        with self.assertRaises(ValueError):
            BlockCommandComponent()

    def test_block_state(self):
        cc = BlockCommandComponent(block_id='dropper', block_state=dict(facing='up'))
        self.assertEqual(cc.block_state, BlockState(facing='up'))

    def test_block_state_safe(self):
        cc = BlockCommandComponent(block_id='dropper')
        self.assertEqual(cc.block_state_safe, BlockState())

    def test_data_tag(self):
        cc = BlockCommandComponent(block_id='dropper', data_tag={'Lock': 'password'})
        self.assertEqual(cc.data_tag, CompoundDataTag({'Lock': 'password'}))

    def test_data_tag_safe(self):
        cc = BlockCommandComponent(block_id='dropper')
        self.assertEqual(cc.data_tag_safe, CompoundDataTag())

    def test_block(self):
        cc = BlockCommandComponent(
            block=BlockEntity(
                block_id='dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}))
        self.assertEqual(cc.block_id, 'dropper')
        self.assertEqual(cc.block_state, BlockState(facing='up'))
        self.assertEqual(cc.data_tag, CompoundDataTag({'Lock': 'password'}))

    def test_block_overwrite(self):
        cc = BlockCommandComponent(
            block=BlockEntity(
                block_id='dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}),
            block_id='dispenser',
            block_state=dict(facing='down'),
            data_tag={'Lock': 'abc123'})
        self.assertEqual(cc.block_id, 'dispenser')
        self.assertEqual(cc.block_state, BlockState(facing='down'))
        self.assertEqual(cc.data_tag, CompoundDataTag({'Lock': 'abc123'}))

    def test_str_block_id(self):
        cc = BlockCommandComponent(
            block_id='dropper')
        self.assertEqual(str(cc), 'dropper')

    def test_str_block_id_and_state(self):
        cc = BlockCommandComponent(
            block_id='dropper',
            block_state=dict(facing='up'))
        self.assertEqual(str(cc), 'dropper[facing=up]')

    def test_str_block_id_and_data_tag(self):
        cc = BlockCommandComponent(
            block_id='dropper',
            data_tag={'Lock': 'password'})
        self.assertEqual(str(cc), 'dropper{Lock:password}')

    def test_str_block_id_and_state_and_data_tag(self):
        cc = BlockCommandComponent(
            block_id='dropper',
            block_state=dict(facing='up'),
            data_tag={'Lock': 'password'})
        self.assertEqual(str(cc), 'dropper[facing=up]{Lock:password}')
