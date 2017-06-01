import unittest

from pymcutil.block.block_entity import BlockEntity
from pymcutil.command import commands


class SetblockCommandTestCase(unittest.TestCase):
    def test_without_any_optionals(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='dropper')
        self.assertEqual(str(cmd), 'setblock 1 2 3 dropper')

    def test_with_block_state(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='dropper',
            block_state=dict(facing='up'))
        self.assertEqual(str(cmd), 'setblock 1 2 3 dropper facing=up')

    def test_with_old_block_handling(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='dropper',
            old_block_handling='destroy')
        self.assertEqual(str(cmd), 'setblock 1 2 3 dropper default destroy')

    def test_with_data_tag(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block_id='dropper',
            data_tag={'Lock': 'password'})
        self.assertEqual(str(cmd), 'setblock 1 2 3 dropper default replace {Lock:password}')

    def test_with_block(self):
        cmd = commands.setblock(
            position=(1, 2, 3),
            block=BlockEntity(
                block_id='dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}))
        self.assertEqual(str(cmd), 'setblock 1 2 3 dropper facing=up replace {Lock:password}')
