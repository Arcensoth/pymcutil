import unittest

from pymcutil.block.block import Block
from pymcutil.block.block_entity import BlockEntity
from pymcutil.command import commands
from pymcutil.position.position import ZERO_OFFSET


class SetblockCommandTestCase(unittest.TestCase):
    def test_block_with_id(self):
        cmd = commands.setblock(
            position=ZERO_OFFSET,
            block='dropper')
        self.assertEqual(str(cmd), 'setblock ~ ~ ~ dropper')

    def test_block_with_id_and_state(self):
        cmd = commands.setblock(
            position=ZERO_OFFSET,
            block=Block(
                block_id='dropper',
                block_state=dict(facing='up')))
        self.assertEqual(str(cmd), 'setblock ~ ~ ~ dropper[facing=up]')

    def test_block_with_id_and_state_and_data_tag(self):
        cmd = commands.setblock(
            position=ZERO_OFFSET,
            block=BlockEntity(
                block_id='dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}))
        self.assertEqual(str(cmd), 'setblock ~ ~ ~ dropper[facing=up]{Lock:password}')

    def test_old_block_handling(self):
        cmd = commands.setblock(
            position=ZERO_OFFSET,
            block='dropper',
            old_block_handling='destroy')
        self.assertEqual(str(cmd), 'setblock ~ ~ ~ dropper destroy')
