import collections
import typing


def no_op_converter(value):
    return value


class RepeatableArgument(collections.Sequence):
    def __init__(self, values: typing.Iterable):
        self.values: list = list(values)

    def __getitem__(self, index):
        return self.values.__getitem__(index)

    def __len__(self):
        return self.values.__len__()

    @classmethod
    def expand(cls, obj, converter: typing.Callable = no_op_converter):
        if obj is None:
            return None

        # Make sure we're dealing with either a `list` or a `tuple` here.
        raw_values = obj if isinstance(obj, (list, tuple)) else (obj,)

        # Convert each value using the given `converter`.
        values = (converter(v) for v in raw_values)

        return cls(values)
