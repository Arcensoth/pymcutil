import unittest

from pymcutil.block import Block
from pymcutil.block_state import BlockState


class BlockTestCase(unittest.TestCase):
    def test_block_with_id(self):
        b = Block('wool')
        self.assertEqual(b.block_id, 'wool')

    def test_block_with_id_and_block_state(self):
        b = Block('wool', BlockState(color='red'))
        self.assertEqual(b.block_id, 'wool')
        self.assertEqual(b.block_state, BlockState(color='red'))

    def test_block_state_from_dict(self):
        b = Block('wool', dict(color='red'))
        self.assertEqual(b.block_state, BlockState(color='red'))

    def test_block_state_from_braces(self):
        b = Block('wool', {'color': 'red'})
        self.assertEqual(b.block_state, BlockState(color='red'))
