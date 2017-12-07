import re
import typing

from pymcutil.util.argument_mapping import ArgumentMapping


class BlockState(ArgumentMapping):
    """ Represents a Minecraft block state. """

    Generic = typing.Mapping

    PATTERN = re.compile('^[a-z0-9_]+$')

    def __setitem__(self, key, value):
        if not (isinstance(key, (bool, int)) or (isinstance(key, str) and self.PATTERN.match(key))):
            raise KeyError('Invalid block state key: {}'.format(key))

        if not (isinstance(value, (bool, int)) or (isinstance(value, str) and self.PATTERN.match(value))):
            raise ValueError('Invalid block state value: {}'.format(value))

        return super().__setitem__(key, value)

    def __str__(self):
        return 'default' if not self else self.innards
