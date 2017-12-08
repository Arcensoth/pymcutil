import collections
import typing

from pymcutil.util.siftable import MappingSiftable


class CommonMapping(collections.MutableMapping, MappingSiftable):
    Generic = typing.Mapping

    def __init__(self, **kwargs):
        self._mapping = {}
        self.update(kwargs)

    def __setitem__(self, key, value):
        return self._mapping.__setitem__(key, value)

    def __delitem__(self, key):
        return self._mapping.__delitem__(key)

    def __getitem__(self, key):
        return self._mapping.__getitem__(key)

    def __len__(self):
        return self._mapping.__len__()

    def __iter__(self):
        return self._mapping.__iter__()
