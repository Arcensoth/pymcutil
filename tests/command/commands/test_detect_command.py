import unittest

from pymcutil.block.block import Block
from pymcutil.block.block_entity import BlockEntity
from pymcutil.command import commands
from pymcutil.position.position import ZERO_OFFSET


class DetectCommandTestCase(unittest.TestCase):
    def test_block_with_id(self):
        cmd = commands.detect(
            position=ZERO_OFFSET,
            block='dropper',
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'detect ~ ~ ~ dropper say hello')

    def test_block_with_id_and_state(self):
        cmd = commands.detect(
            position=ZERO_OFFSET,
            block=Block(
                block_id='dropper',
                block_state=dict(facing='up')),
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'detect ~ ~ ~ dropper[facing=up] say hello')

    def test_block_with_id_and_state_and_data_tag(self):
        cmd = commands.detect(
            position=ZERO_OFFSET,
            block=BlockEntity(
                block_id='dropper',
                block_state=dict(facing='up'),
                data_tag={'Lock': 'password'}),
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'detect ~ ~ ~ dropper[facing=up]{Lock:password} say hello')
