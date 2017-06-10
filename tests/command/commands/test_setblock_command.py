import unittest

from pymcutil.block.block_entity import BlockEntity
from pymcutil.command import commands


class SetblockCommandTestCase(unittest.TestCase):
    def test_without_any_optionals(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='minecraft:dropper')
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper')

    def test_default_optionals(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='minecraft:dropper',
            data_tag={})
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper default replace {}')

    def test_up_to_block_state(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='minecraft:dropper',
            block_state=dict(facing='up'))
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper facing=up')

    def test_up_to_old_block_handling(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='minecraft:dropper',
            block_state=dict(facing='up'),
            old_block_handling='destroy')
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper facing=up destroy')

    def test_up_to_data_tag(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='minecraft:dropper',
            block_state=dict(facing='up'),
            old_block_handling='destroy',
            data_tag={'Lock': 'password'})
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper facing=up destroy {Lock:password}')

    def test_with_block(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block=BlockEntity(
                block_id='minecraft:dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}))
        self.assertEqual(str(cmd), 'setblock 1 2 3 minecraft:dropper facing=up replace {Lock:password}')
