from collections import Iterable, MutableSequence

from pymcutil.data_tag import DataTag
from pymcutil.data_tag.helper import data_taggify
from pymcutil.util.siftable import SequenceSiftable


class ListDataTag(DataTag, MutableSequence, SequenceSiftable):
    """ A list data tag, also known as TAG_List. """

    Generic = Iterable

    def __init__(self, *args):
        self._value = []

        # If the only thing supplied is an iterable, then append everything from it.
        if len(args) == 1 and isinstance(args[0], Iterable):
            for item in args[0]:
                self.append(item)

        # Otherwise, append everything given.
        else:
            for arg in args:
                self.append(arg)

    def __delitem__(self, index):
        return self._value.__delitem__(index)

    def __setitem__(self, index, value):
        value = data_taggify(value)
        return self._value.__setitem__(index, value)

    def __len__(self):
        return self._value.__len__()

    def __getitem__(self, index):
        return self._value.__getitem__(index)

    def __eq__(self, other):
        return isinstance(other, ListDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> list:
        return self._value

    def insert(self, index, value):
        value = data_taggify(value)
        return self._value.insert(index, value)

    def to_str(self) -> str:
        items = (str(item) for item in self)
        return ''.join(('[', ','.join(items), ']'))
