import typing
from numbers import Real
from typing import Iterable, Union

from pymcutil.util.siftable import Siftable


class Range(Siftable):
    """
    Represents numeric ranges as they appear in selectors:

        level=10 is level 10
        level=10..12 is level 10, 11 or 12
        level=5.. is anything level 5 or above
        level=..15 is anything level 15 or below

    Supports unbounded minimum, maximum, and exact values by (ab)using the builtin `...` (`Ellipsis`) constant:

        Range(1) => 1
        Range(1, ...) => 1..
        Range(..., 2) => ..2
        Range(1, 2) => 1..2

    Any numeric, iterable, or string objects may be implicitly converted in context:

        1 => Range(1)
        (1, ...) => Range(1, ...)
        [..., 2] => Range(..., 2)
        '1..2' => Range(1, 2)

    """

    Generic = Union['Range', Real, Iterable, str]

    @classmethod
    def _from_other(cls, obj):
        if isinstance(obj, Real):
            return cls.from_real(obj)
        elif isinstance(obj, str):
            return cls.from_string(obj)
        elif isinstance(obj, Iterable):
            return cls.from_iterable(obj)

    @classmethod
    def from_real(cls, n: Real):
        """ Convert real numbers as is_exact values. """
        return cls(n)

    @classmethod
    def from_iterable(cls, i: Iterable):
        """ Convert tuples and lists. """
        return cls(*i)

    @classmethod
    def from_string(cls, s: str):
        """ Convert strings from their natural form. """
        # TODO use regex
        parts = s.split('..')
        min_str = parts[0]
        max_str = parts[1] if len(parts) > 1 else None
        min_ = float(min_str) if min_str else ...
        max_ = float(max_str) if max_str else (... if max_str == '' else None)
        return cls(min_, max_)

    def __init__(self, min_: Real, max_: Real = None):
        self._min: Real = min_
        self._max: Real = max_ if max_ is not None else min_  # Range(1) => Range(1, 1)

    def __str__(self):
        min_str = '{:g}'.format(self.min) if isinstance(self.min, Real) else ''
        if self.is_exact:
            return min_str
        max_str = '{:g}'.format(self.max) if isinstance(self.max, Real) else ''
        return '{}..{}'.format(min_str, max_str)

    def __eq__(self, other):
        return isinstance(other, Range) \
               and isinstance(other, self.__class__) \
               and (self.min == other.min) \
               and (self.max == other.max)

    @property
    def min(self) -> typing.Union[Real, None]:
        return self._min

    @property
    def max(self) -> typing.Union[Real, None]:
        return self._max

    @property
    def is_exact(self) -> bool:
        return isinstance(self.min, Real) and (self.min == self.max)
