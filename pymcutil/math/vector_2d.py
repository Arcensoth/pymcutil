from pymcutil.math.vector import Vector


class Vector2D(Vector):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    @property
    def x(self) -> float:
        return self._components[0]

    @property
    def y(self) -> float:
        return self._components[1]
