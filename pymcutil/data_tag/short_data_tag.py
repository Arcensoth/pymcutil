from pymcutil.constants import SHORT_MIN, SHORT_MAX
from pymcutil.data_tag import DataTag


class ShortDataTag(DataTag):
    """ A short data tag, also known as TAG_Short. """

    def __init__(self, value=0):
        self._value: int = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, ShortDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        value = int(value)
        if not (SHORT_MIN <= value <= SHORT_MAX):
            raise ValueError(f'Value exceeds capacity of a short: {value}')
        self._value = value

    def to_str(self) -> str:
        return f'{self.value}s'
