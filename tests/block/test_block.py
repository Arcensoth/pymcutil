import unittest

from pymcutil.block.block import Block
from pymcutil.block.block_state import BlockState


class BlockTestCase(unittest.TestCase):
    def test_block_with_id(self):
        b = Block('piston')
        self.assertEqual(b.block_id, 'piston')

    def test_block_with_id_and_block_state(self):
        b = Block('piston', BlockState(facing='up'))
        self.assertEqual(b.block_id, 'piston')
        self.assertEqual(b.block_state, BlockState(facing='up'))

    def test_block_state_from_dict(self):
        b = Block('piston', dict(facing='up'))
        self.assertEqual(b.block_state, BlockState(facing='up'))

    def test_block_state_from_braces(self):
        b = Block('piston', {'facing': 'up'})
        self.assertEqual(b.block_state, BlockState(facing='up'))

    def test_state(self):
        b1 = Block('piston')
        b2 = b1.state(facing='up')
        self.assertEqual(b1.block_id, 'piston')
        self.assertEqual(b1.block_state, BlockState())
        self.assertEqual(b2.block_id, 'piston')
        self.assertEqual(b2.block_state, BlockState(facing='up'))

    def test_state_overwrite(self):
        b1 = Block('piston', dict(facing='up'))
        b2 = b1.state(facing='down')
        self.assertEqual(b1.block_id, 'piston')
        self.assertEqual(b1.block_state, BlockState(facing='up'))
        self.assertEqual(b2.block_id, 'piston')
        self.assertEqual(b2.block_state, BlockState(facing='down'))

    def test_state_more(self):
        b1 = Block('piston', dict(facing='up'))
        b2 = b1.state(extended=True)
        self.assertEqual(b1.block_id, 'piston')
        self.assertEqual(b1.block_state, BlockState(facing='up'))
        self.assertEqual(b2.block_id, 'piston')
        self.assertEqual(b2.block_state, BlockState(facing='up', extended=True))
