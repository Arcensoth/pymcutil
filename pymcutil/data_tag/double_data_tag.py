from pymcutil.data_tag import DataTag


class DoubleDataTag(DataTag):
    """ A double data tag, also known as TAG_Double. """

    def __init__(self, value=0):
        self._value: float = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, DoubleDataTag) and self.value.__eq__(other.value)

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value):
        value = float(value)
        self._value = value

    def to_str(self) -> str:
        return f'{self.value}d'
