import unittest

from pymcutil.math.vector_3d import Vector3D


class Vector3DTestCase(unittest.TestCase):
    def test_init(self):
        v = Vector3D(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_str(self):
        self.assertEqual(str(Vector3D(1, 2, 3)), '1 2 3')
