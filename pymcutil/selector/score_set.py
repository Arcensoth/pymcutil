from pymcutil.util.argument_mapping import ArgumentMapping
from pymcutil.selector.range import Range


class ScoreSet(ArgumentMapping):
    def __setitem__(self, key, value):
        value = Range.sift(value, None)
        if value is None:
            raise ValueError('Value {} cannot be converted to a valid range'.format(value))
        super().__setitem__(key, value)
