from pymcutil.position.rc import RC
from pymcutil.position.vector_2d import Vector2D


class Rotation(Vector2D):
    """ Rotation representation using yaw and pitch. Includes relative capabilities. """

    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def __invert__(self):
        return self.relative()

    def __abs__(self):
        return self.absolute()

    def relative(self):
        return self.__class__(*[RC(c) for c in self.components])

    def absolute(self):
        return self.__class__(*[float(c) for c in self.components])

    @property
    def yaw(self):
        return self.x

    @property
    def pitch(self):
        return self.y


ZERO_ROTATION = Rotation(0, 0)
ZERO_TURN = ~ZERO_ROTATION
