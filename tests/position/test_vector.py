import unittest

from pymcutil.position.vector import Vector


class VectorTestCase(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Vector(1, 2)), 'Vector(1.0, 2.0)')

    def test_str(self):
        self.assertEqual(str(Vector(1, 2)), '1 2')

    def test_to_int_str(self):
        self.assertEqual(Vector(1, 2.5).to_int_str(), '1 2')

    def test_to_float_str(self):
        self.assertEqual(Vector(1, 2.5).to_float_str(), '1 2.5')

    def test_to_int_list(self):
        self.assertEqual(Vector(1, 2.5).to_int_list(), [1, 2])

    def test_to_float_list(self):
        self.assertEqual(Vector(1, 2.5).to_float_list(), [1.0, 2.5])

    # ---- eq ----------------------------------------------------------------------------------------------------------

    def test_eq(self):
        self.assertEqual(Vector(1, 2), Vector(1.0, 2.0))

    def test_not_eq(self):
        self.assertNotEqual(Vector(1, 2), Vector(1.0, 1.0))

    def test_really_not_eq(self):
        self.assertNotEqual(Vector(1, 2), Vector(2.0, 1.0))

    def test_definitely_not_eq(self):
        self.assertNotEqual(Vector(1, 2), Vector(1, 2, 3))

    def test_really_definitely_not_eq(self):
        self.assertNotEqual(Vector(1, 2), 'incompatible')

    # ---- add ---------------------------------------------------------------------------------------------------------

    def test_add_with_int(self):
        self.assertEqual(Vector(1, 2) + 1, Vector(2, 3))

    def test_add_with_float(self):
        self.assertEqual(Vector(1, 2) + 0.5, Vector(1.5, 2.5))

    def test_add_with_vector(self):
        self.assertEqual(Vector(1, 2) + Vector(2, 3), Vector(3, 5))

    def test_add_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2) + 'incompatible'

    def test_add_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2) + Vector(1, 2, 3)

    # ---- sub ---------------------------------------------------------------------------------------------------------

    def test_sub_with_int(self):
        self.assertEqual(Vector(1, 2) - 1, Vector(0, 1))

    def test_sub_with_float(self):
        self.assertEqual(Vector(1, 2) - 0.5, Vector(0.5, 1.5))

    def test_sub_with_vector(self):
        self.assertEqual(Vector(3, 5) - Vector(2, 3), Vector(1, 2))

    def test_sub_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2) - 'incompatible'

    def test_sub_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(3, 5) - Vector(2, 3, 4)

    # ---- mul ---------------------------------------------------------------------------------------------------------

    def test_mul_with_int(self):
        self.assertEqual(Vector(1, 2) * 2, Vector(2, 4))

    def test_mul_with_float(self):
        self.assertEqual(Vector(1, 2) * 0.5, Vector(0.5, 1))

    def test_mul_with_vector(self):
        self.assertEqual(Vector(1, 2) * Vector(2, 3), Vector(2, 6))

    def test_mul_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2) * 'incompatible'

    def test_mul_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2) * Vector(2, 3, 4)

    # ---- truediv -----------------------------------------------------------------------------------------------------

    def test_truediv_with_int(self):
        self.assertEqual(Vector(7, 4) / 2, Vector(3.5, 2))

    def test_truediv_with_float(self):
        self.assertEqual(Vector(1.25, 2.1) / 0.5, Vector(2.5, 4.2))

    def test_truediv_with_vector(self):
        self.assertEqual(Vector(7, 4) / Vector(2, 5), Vector(3.5, 0.8))

    def test_truediv_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(7, 4) / 'incompatible'

    def test_truediv_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(7, 4) / Vector(1, 2, 3)

    # ---- floordiv ----------------------------------------------------------------------------------------------------

    def test_floordive_with_int(self):
        self.assertEqual(Vector(7, 4) // 2, Vector(3, 2))

    def test_floordive_with_float(self):
        self.assertEqual(Vector(1.25, 2.1) // 0.5, Vector(2, 4))

    def test_floordive_with_vector(self):
        self.assertEqual(Vector(7, 4) // Vector(2, 5), Vector(3, 0))

    def test_floordive_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(7, 4) // 'incompatible'

    def test_floordive_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(7, 4) // Vector(1, 2, 3)

    # ---- others ------------------------------------------------------------------------------------------------------

    def test_iadd(self):
        v = Vector(1, 2)
        v += Vector(2, 3)
        self.assertEqual(v, Vector(3, 5))

    def test_isub(self):
        rc = Vector(3, 5)
        rc -= Vector(2, 3)
        self.assertEqual(rc, Vector(1, 2))

    def test_imul(self):
        rc = Vector(1, 2)
        rc *= Vector(2, 3)
        self.assertEqual(rc, Vector(2, 6))

    def test_itruediv(self):
        rc = Vector(7, 4)
        rc /= Vector(2, 5)
        self.assertEqual(rc, Vector(3.5, 0.8))

    def test_ifloordiv(self):
        rc = Vector(7, 4)
        rc //= Vector(2, 5)
        self.assertEqual(rc, Vector(3, 0))

    def test_radd(self):
        with self.assertRaises(TypeError):
            'incompatible' + Vector(1, 2)

    def test_rmul(self):
        with self.assertRaises(TypeError):
            'incompatible' * Vector(1, 2)

    def test_neg(self):
        self.assertEqual(-Vector(1, 2), Vector(-1, -2))

    def test_iter(self):
        self.assertEqual([c for c in Vector(1, 2, 3)], [1, 2, 3])

    # ------------------------------------------------------------------------------------------------------------------

    def test_components(self):
        self.assertEqual(Vector(1, 2).components, [1, 2])

    def test_magnitude(self):
        self.assertEqual(Vector(2, 3, 0.5).magnitude, 3)

    def test_expand(self):
        self.assertEqual(Vector(1, 2).expand(Vector(3, 1)), Vector(3, 2))

    def test_expand_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2).expand('incompatible')

    def test_expand_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2).expand(Vector(3, 1, 0))

    def test_contract(self):
        self.assertEqual(Vector(3, 2).contract(Vector(1, 3)), Vector(1, 2))

    def test_contract_incompatible_type_error(self):
        with self.assertRaises(TypeError):
            Vector(3, 2).contract('incompatible')

    def test_contract_incompatible_vector_error(self):
        with self.assertRaises(TypeError):
            Vector(3, 2).contract(Vector(1, 2, 0))
