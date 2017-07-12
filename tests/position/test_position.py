import unittest

from pymcutil.position.position import Position, ZERO_POSITION, ZERO_OFFSET
from pymcutil.position.rc import rel


class PositionTestCase(unittest.TestCase):
    def test_init(self):
        p = Position(1, 2, 3)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)

    def test_invert(self):
        self.assertEqual(str(~Position(1, 2, 3)), '~1 ~2 ~3')

    def test_abs(self):
        self.assertEqual(str(abs(~Position(1, 2, 3))), '1 2 3')

    def test_zero_position(self):
        self.assertEqual(str(ZERO_POSITION), '0 0 0')

    def test_zero_offset(self):
        self.assertEqual(str(ZERO_OFFSET), '~ ~ ~')

    def test_rel_mixed_zero_coords(self):
        self.assertEqual(str(~Position(4, 0, 4)), '~4 ~ ~4')

    def test_rel_decimal_coords(self):
        self.assertEqual(str(~Position(3.142, 6.674, 2.718)), '~3.142 ~6.674 ~2.718')

    def test_mixed_abs_and_rel_coords(self):
        self.assertEqual(str(Position(1, rel(2), 3)), '1 ~2 3')

    def test_mixed_abs_and_rel_to_rel_coords(self):
        self.assertEqual(str(~Position(1, rel(2), 3)), '~1 ~2 ~3')
