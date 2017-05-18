import unittest

from pymcutil.block import Block
from pymcutil.block_state import BlockState


class BlockTestCase(unittest.TestCase):
    def test_block_with_state(self):
        b = Block('wool', BlockState(color='red'))
        self.assertEqual(b.block_id, 'wool')
        self.assertEqual(b.block_state, BlockState(color='red'))
