import re

from pymcutil.data_tag import DataTag


class StringDataTag(DataTag):
    """ A string data tag, also known as TAG_String. """

    PATTERN = re.compile('^[a-zA-Z0-9._+\-]+$')

    def __init__(self, value=''):
        self._value: str = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, StringDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        value = str(value)
        self._value = value

    def to_str(self) -> str:
        # If the string contains syntax-breaking characters, it needs to be surrounded with quotes and any existing
        # quotes need to be escaped.
        if not self.PATTERN.match(self.value):
            return ''.join(('"', self.value.replace('"', '\\"'), '"'))
        return self.value
