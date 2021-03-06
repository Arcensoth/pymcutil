from pymcutil.data_tag import DataTag


class FloatDataTag(DataTag):
    """ A float data tag, also known as TAG_Float. """

    def __init__(self, value=0.0):
        self._value: float = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, FloatDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value):
        self._value = float(value)

    def to_str(self) -> str:
        return f'{self.value}f'
