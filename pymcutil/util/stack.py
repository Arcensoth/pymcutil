from collections import MutableSequence
from typing import Iterable


class Stack(MutableSequence):
    def __init__(self, items: Iterable = ()):
        self._items = list(items)

    def __getitem__(self, index):
        return self._items.__getitem__(index)

    def __setitem__(self, index, value):
        return self._items.__setitem__(index, value)

    def __delitem__(self, index):
        return self._items.__delitem__(index)

    def __len__(self):
        return self._items.__len__()

    def insert(self, index, value):
        return self._items.insert(index, value)

    def push(self, value):
        self._items.append(value)

    def empty(self) -> bool:
        return not bool(self)
