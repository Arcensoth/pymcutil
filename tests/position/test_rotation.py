import unittest

from pymcutil.position.rc import rel
from pymcutil.position.rotation import Rotation, ZERO_ROTATION, ZERO_TURN


class RotationTestCase(unittest.TestCase):
    def test_init(self):
        r = Rotation(45, 90)
        self.assertEqual(r.yaw, 45)
        self.assertEqual(r.pitch, 90)

    def test_invert(self):
        self.assertEqual(str(~Rotation(45, 90)), '~45 ~90')

    def test_abs(self):
        self.assertEqual(str(abs(~Rotation(45, 90))), '45 90')

    def test_zero_rotation(self):
        self.assertEqual(str(ZERO_ROTATION), '0 0')

    def test_zero_turn(self):
        self.assertEqual(str(ZERO_TURN), '~ ~')

    def test_rel_mixed_zero_coords(self):
        self.assertEqual(str(~Rotation(0, 30)), '~ ~30')

    def test_rel_decimal_coords(self):
        self.assertEqual(str(~Rotation(3.142, 6.674)), '~3.142 ~6.674')

    def test_mixed_abs_and_rel_coords(self):
        self.assertEqual(str(Rotation(45, rel(30))), '45 ~30')

    def test_mixed_abs_and_rel_to_rel_coords(self):
        self.assertEqual(str(~Rotation(45, rel(90))), '~45 ~90')
