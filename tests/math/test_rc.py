import unittest

from pymcutil.math.rc import RC, rel


class PositionTestCase(unittest.TestCase):
    def test_rel(self):
        self.assertEqual(rel(1), RC(1))

    def test_repr(self):
        self.assertEqual(repr(RC(1)), 'RC(1.0)')

    def test_str(self):
        self.assertEqual(str(RC(1)), '~1.0')

    def test_zero_str(self):
        self.assertEqual(str(RC(0)), '~')

    def test_eq(self):
        self.assertEqual(RC(1), RC(1.0))

    # TODO Decide whether a relative coord should be equal to an absolute coord.
    # Probably not, but it seems we have an issue with inheriting float in that comparing to any builtin value
    # will fallback to float's equivalency method, overriding ours. Perhaps we need to componentize the float instead.

    # def test_not_eq_to_float(self):
    #     self.assertNotEqual(RC(1), 1.0)
    #
    # def test_not_eq_to_int(self):
    #     self.assertNotEqual(RC(1), 1)

    def test_not_eq_to_str(self):
        self.assertNotEqual(RC(1), 'incompatible')

    def test_add(self):
        self.assertEqual(RC(1) + RC(2), RC(3))

    def test_add_error(self):
        with self.assertRaises(TypeError):
            RC(1) + 'incompatible'

    def test_sub(self):
        self.assertEqual(RC(3) - RC(2), RC(1))

    def test_sub_error(self):
        with self.assertRaises(TypeError):
            RC(3) - 'incompatible'

    def test_mul(self):
        self.assertEqual(RC(3) * RC(2), RC(6))

    def test_mul_error(self):
        with self.assertRaises(TypeError):
            RC(3) * 'incompatible'

    def test_truediv(self):
        self.assertEqual(RC(7) / RC(2), RC(3.5))

    def test_truediv_error(self):
        with self.assertRaises(TypeError):
            RC(7) / 'incompatible'

    def test_floordiv(self):
        self.assertEqual(RC(7) // RC(2), RC(3))

    def test_floordiv_error(self):
        with self.assertRaises(TypeError):
            RC(7) // 'incompatible'

    def test_iadd(self):
        rc = RC(1)
        rc += RC(2)
        self.assertEqual(rc, RC(3))

    def test_isub(self):
        rc = RC(3)
        rc -= RC(2)
        self.assertEqual(rc, RC(1))

    def test_imul(self):
        rc = RC(3)
        rc *= RC(2)
        self.assertEqual(rc, RC(6))

    def test_itruediv(self):
        rc = RC(7)
        rc /= RC(2)
        self.assertEqual(rc, RC(3.5))

    def test_ifloordiv(self):
        rc = RC(7)
        rc //= RC(2)
        self.assertEqual(rc, RC(3))

    def test_radd(self):
        with self.assertRaises(TypeError):
            'incompatible' + RC(2)

    def test_rmul(self):
        with self.assertRaises(TypeError):
            'incompatible' * RC(2)

    def test_neg(self):
        self.assertEqual(-RC(1), RC(-1))
