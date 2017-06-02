import unittest

from pymcutil.block.block_state import BlockState
from pymcutil.position.position import Position


class SiftableTestCase(unittest.TestCase):
    def test_sift_position_from_tuple(self):
        self.assertEqual(Position.sift((1, 2, 3)), Position(1, 2, 3))

    def test_sift_position_from_list(self):
        self.assertEqual(Position.sift([1, 2, 3]), Position(1, 2, 3))

    def test_sift_position_from_dict(self):
        self.assertEqual(Position.sift({1: 'one', 2: 'two', 3: 'three'}), Position(1, 2, 3))

    def test_sift_position_from_position(self):
        self.assertEqual(Position.sift(Position(1, 2, 3)), Position(1, 2, 3))

    def test_sift_block_state_from_dict(self):
        self.assertEqual(BlockState.sift({'a': 'alpha', 'b': 'beta'}), BlockState(a='alpha', b='beta'))

    def test_sift_block_state_from_block_state(self):
        self.assertEqual(BlockState.sift(BlockState(a='alpha', b='beta')), BlockState(a='alpha', b='beta'))

    def test_siftable_default(self):
        self.assertEqual(Position.sift(None, (1, 2, 3)), Position(1, 2, 3))

    def test_siftable_empty_default(self):
        self.assertIsNone(Position.sift(None, None))

    def test_sift_value_error(self):
        with self.assertRaises(ValueError):
            Position.sift(None)

    def test_sift_type_error(self):
        with self.assertRaises(TypeError):
            Position.sift(42)
