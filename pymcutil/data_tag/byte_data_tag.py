from pymcutil.constants import BYTE_MIN, BYTE_MAX
from pymcutil.data_tag import DataTag


class ByteDataTag(DataTag):
    """ A byte data tag, also known as TAG_Byte. """

    def __init__(self, value=0):
        self._value: int = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, ByteDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        value = int(value)
        if not (BYTE_MIN <= value <= BYTE_MAX):
            raise ValueError(f'Value exceeds capacity of a byte: {value}')
        self._value = value

    def to_str(self) -> str:
        return f'{self.value}b'
