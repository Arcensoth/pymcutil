import re
from collections import MutableMapping


class BlockState(MutableMapping):
    """ Represents a Minecraft block state. """

    pattern = re.compile('^[a-z0-9_]+$')

    def __init__(self, **kwargs):
        self._mapping = {}
        self.update(kwargs)

    def __delitem__(self, key):
        return self._mapping.__delitem__(key)

    def __iter__(self):
        return self._mapping.__iter__()

    def __setitem__(self, key, value):
        if not (isinstance(key, (bool, int)) or (isinstance(key, str) and self.pattern.match(key))):
            raise KeyError(f'Invalid block state key: {key}')

        if not (isinstance(value, (bool, int)) or (isinstance(value, str) and self.pattern.match(value))):
            raise ValueError(f'Invalid block state value: {value}')

        return self._mapping.__setitem__(key, value)

    def __len__(self):
        return self._mapping.__len__()

    def __getitem__(self, key):
        return self._mapping.__getitem__(key)

    def __str__(self):
        return 'default' if not self else ','.join([f'{k}={self._convert(v)}' for k, v in self.items()])

    @staticmethod
    def _convert(value):
        if isinstance(value, bool):
            return 'true' if value else 'false'
        return value
