from collections import MutableMapping

from pymcutil.data_tag import DataTag
from pymcutil.data_tag.helper import data_taggify
from pymcutil.data_tag.string_data_tag import StringDataTag


class CompoundDataTag(DataTag, MutableMapping):
    """ A compound data tag, also known as TAG_Compound. """

    def __init__(self, *args, **kwargs):
        self._mapping = {}
        for arg in args:
            self.update(**arg)
        self.update(kwargs)

    def __delitem__(self, key):
        return self._mapping.__delitem__(key)

    def __iter__(self):
        return self._mapping.__iter__()

    def __setitem__(self, key, value):
        key = str(key)
        value = data_taggify(value)
        return self._mapping.__setitem__(key, value)

    def __len__(self):
        return self._mapping.__len__()

    def __getitem__(self, key):
        return self._mapping.__getitem__(key)

    def to_str(self) -> str:
        # Keys are strings and use the same syntax rules as NBT strings.
        pairs = (f'{StringDataTag(key)}:{value}' for key, value in self.items())
        return ''.join(('{', ','.join(pairs), '}'))
