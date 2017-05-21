import unittest

from pymcutil.position.vector_2d import Vector2D


class Vector2DTestCase(unittest.TestCase):
    def test_init(self):
        v = Vector2D(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_str(self):
        self.assertEqual(str(Vector2D(1, 2)), '1 2')
