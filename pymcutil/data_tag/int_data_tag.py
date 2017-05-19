from pymcutil.constants import INT_MIN, INT_MAX
from pymcutil.data_tag import DataTag


class IntDataTag(DataTag):
    """ An int data tag, also known as TAG_Int. """

    def __init__(self, value=0):
        self._value: int = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, IntDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        value = int(value)
        if not (INT_MIN <= value <= INT_MAX):
            raise ValueError(f'Value exceeds capacity of an int: {value}')
        self._value = value

    def to_str(self) -> str:
        # Ints are the default data tag for any integer value, and lack a suffix entirely.
        return f'{self.value}'
