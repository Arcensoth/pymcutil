from pymcutil.math.vector import Vector


class Vector3D(Vector):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)

    @property
    def x(self) -> float:
        return self._components[0]

    @property
    def y(self) -> float:
        return self._components[1]

    @property
    def z(self) -> float:
        return self._components[2]
