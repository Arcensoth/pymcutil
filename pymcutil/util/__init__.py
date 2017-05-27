def default(value, default_=None):
    return default_ if value is None else value


def defaults(original: dict, **kwargs):
    kwargs.update(original)
    return kwargs


def first(*args):
    return next((item for item in args if item is not None), None)
