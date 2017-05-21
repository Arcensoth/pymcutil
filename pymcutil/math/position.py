from pymcutil.math.rc import RC
from pymcutil.math.vector_3d import Vector3D


class Position(Vector3D):
    """ Position AKA location representation containing x, y, z coordinates that may be relative. Note that all
    math operations are defined under the inherited Vector class, meaning we can conveniently add, subtract, etc
    positions from one another. We can also make a position relative by invoking the ~ operator on it, or turn
    individual coordinates relative by explicitly using the RC class. """

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)

    def __invert__(self):
        return self.__class__(*[RC(c) for c in self.components])


ZERO_POSITION = Position(0, 0, 0)
SELF_POSITION = ~ZERO_POSITION
