from pymcutil.position.rc import RC
from pymcutil.position.vector_3d import Vector3D


class Position(Vector3D):
    """ Position AKA location representation containing x, y, z coordinates that may be relative. Note that all
    position operations are defined under the inherited Vector class, meaning we can conveniently add, subtract, etc
    positions from one another. We can also make a position relative by invoking the ~ operator on it, or turn
    individual coordinates relative by explicitly using the RC class. """

    @classmethod
    def _from_other(cls, obj):
        # A tuple `(x, y, z)` will produce relative coordinates, whereas everything else (such as a list `[x, y, z]`)
        # will instead produce absolute coordinates.
        sifted = super()._from_other(obj)
        return ~sifted if isinstance(obj, tuple) else sifted

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)

    def __invert__(self):
        return self.relative()

    def __abs__(self):
        return self.absolute()

    def relative(self):
        return self.__class__(*[RC(c) for c in self.components])

    def absolute(self):
        return self.__class__(*[float(c) for c in self.components])


ZERO_POSITION = Position(0, 0, 0)
ZERO_OFFSET = ~ZERO_POSITION
BELOW_OFFSET = ~Position(0, -1, 0)
ABOVE_OFFSET = ~Position(0, 1, 0)
