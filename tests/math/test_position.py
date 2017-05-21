import unittest

from pymcutil.math.position import Position, ZERO_POSITION, SELF_POSITION


class PositionTestCase(unittest.TestCase):
    def test_init(self):
        p = Position(1, 2, 3)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)

    def test_invert(self):
        self.assertEqual(str(~Position(1, 2, 3)), '~1 ~2 ~3')

    def test_zero_position(self):
        self.assertEqual(str(ZERO_POSITION), '0 0 0')

    def test_self_position(self):
        self.assertEqual(str(SELF_POSITION), '~ ~ ~')

    def test_abs_plus_rel(self):
        self.assertEqual(Position(1, 2, 3) + ~Position(4, 5, 6), ~Position(5, 7, 9))
