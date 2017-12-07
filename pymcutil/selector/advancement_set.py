from pymcutil.util.argument_mapping import ArgumentMapping


class AdvancementSet(ArgumentMapping):
    def __setitem__(self, key, value):
        if not isinstance(value, bool):
            value = ArgumentMapping.sift(value, None)
            if value is None:
                raise ValueError('Value {} is neither a bool nor another mapping'.format(value))
        super().__setitem__(key, value)

