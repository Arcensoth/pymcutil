import collections
from typing import Union

from pymcutil.util.siftable import Siftable


class Symbol(Siftable, collections.Hashable):
    Generic = Union['Symbol', str]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Symbol) and \
               isinstance(other, self.__class__) \
               and (other.value == self.value)

    @classmethod
    def _from_other(cls, obj):
        if isinstance(obj, str):
            return cls(obj)
