from collections import Mapping, MutableMapping

from pymcutil.data_tag import DataTag
from pymcutil.data_tag.helper import data_taggify
from pymcutil.data_tag.string_data_tag import StringDataTag
from pymcutil.util.siftable import MappingSiftable


class CompoundDataTag(DataTag, MutableMapping, MappingSiftable):
    """ A compound data tag, also known as TAG_Compound. """

    Generic = Mapping

    def __init__(self, *args, **kwargs):
        self._value = {}

        # Assume all unnamed args are mappings that can be inherited from.
        for arg in args:
            self.update(**arg)

        # Update from all named args.
        self.update(kwargs)

    def __delitem__(self, key):
        return self._value.__delitem__(key)

    def __iter__(self):
        return self._value.__iter__()

    def __setitem__(self, key, value):
        key = str(key)
        value = data_taggify(value)
        return self._value.__setitem__(key, value)

    def __len__(self):
        return self._value.__len__()

    def __getitem__(self, key):
        return self._value.__getitem__(key)

    def __eq__(self, other):
        return isinstance(other, CompoundDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> dict:
        return self._value

    def to_str(self) -> str:
        # Keys are strings and use the same syntax rules as NBT strings.
        pairs = (f'{StringDataTag(key)}:{value}' for key, value in self.items())
        return ''.join(('{', ','.join(pairs), '}'))
