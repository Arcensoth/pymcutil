import unittest

from pymcutil.block import Block
from pymcutil.block_state import BlockState


class BlockTestCase(unittest.TestCase):
    def test_block_with_state(self):
        b = Block('wool', BlockState(color='red'))
        self.assertEqual(b.block_id, 'wool')
        self.assertEqual(b.block_state, BlockState(color='red'))

    def test_block_with_kwargs(self):
        b = Block('slab', variant='quartz')
        self.assertEqual(b.block_id, 'slab')
        self.assertEqual(b.block_state, BlockState(variant='quartz'))

    def test_block_with_state_and_kwargs(self):
        b = Block('slab', BlockState(half='bottom'), variant='quartz')
        self.assertEqual(b.block_id, 'slab')
        self.assertEqual(b.block_state, BlockState(half='bottom', variant='quartz'))
