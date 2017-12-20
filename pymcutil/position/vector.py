from typing import Iterable, List, Union

from pymcutil.util.siftable import SequenceSiftable


class Vector(Iterable, SequenceSiftable):
    Generic = Union['Vector', Iterable]

    def __init__(self, *components):
        # Don't cast potential subtypes of float into normal floats!
        self._components = [c if isinstance(c, float) else float(c) for c in components]

    def __repr__(self):
        return '{name}({params})'.format(
            name=self.__class__.__name__,
            params=', '.join(['{!r}'.format(c) for c in self.components]))

    def __str__(self):
        return self.to_str()

    def __eq__(self, other):
        if type(other) is type(self) and len(self.components) == len(other.components):
            for c1, c2 in zip(self.components, other.components):
                if c1 != c2:
                    return False
            return True
        return False

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(*[c + other for c in self.components])
        elif isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[c1 + c2 for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot add with {other!r}'.format(self=self, other=other))

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(*[c - other for c in self.components])
        elif isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[c1 - c2 for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot sub with {other!r}'.format(self=self, other=other))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(*[c * other for c in self.components])
        elif isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[c1 * c2 for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot mul with {other!r}'.format(self=self, other=other))

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(*[c / other for c in self.components])
        elif isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[c1 / c2 for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot truediv with {other!r}'.format(self=self, other=other))

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(*[c // other for c in self.components])
        elif isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[c1 // c2 for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot floordiv with {other!r}'.format(self=self, other=other))

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __iter__(self):
        return self.components.__iter__()

    def to_str(self) -> str:
        return ' '.join(['{:g}'.format(c) for c in self.components])

    def to_int_str(self) -> str:
        return ' '.join(['{:d}'.format(c) for c in self.to_int_list()])

    def to_float_str(self) -> str:
        return ' '.join(['{:g}'.format(c) for c in self.to_float_list()])

    def to_int_list(self) -> List[int]:
        return [int(c) for c in self.components]

    def to_float_list(self) -> List[float]:
        return [float(c) for c in self.components]

    def expand(self, other):
        if isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[max(c1, c2) for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot expand with {other!r}'.format(self=self, other=other))

    def contract(self, other):
        if isinstance(other, type(self)) and len(self.components) == len(other.components):
            return self.__class__(*[min(c1, c2) for c1, c2 in zip(self.components, other.components)])
        raise TypeError('{self!r} cannot contract with {other!r}'.format(self=self, other=other))

    @property
    def components(self) -> List[float]:
        return self._components

    @property
    def magnitude(self) -> float:
        m = 1.0
        for c in self.components:
            m *= c
        return m
