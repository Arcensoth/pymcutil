from pymcutil.constants import LONG_MIN, LONG_MAX
from pymcutil.data_tag import DataTag


class LongDataTag(DataTag):
    """ A long data tag, also known as TAG_Long. """

    def __init__(self, value=0):
        self._value: int = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, LongDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        value = int(value)
        if not (LONG_MIN <= value <= LONG_MAX):
            raise ValueError(f'Value exceeds capacity of a long: {value}')
        self._value = value

    def to_str(self) -> str:
        return f'{self.value}l'
