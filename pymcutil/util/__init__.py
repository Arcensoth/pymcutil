import logging


def default(value, default_=None):
    return default_ if value is None else value


def defaults(original: dict, **kwargs):
    kwargs.update(original)
    return kwargs


def first(*args):
    return next((item for item in args if item is not None), None)


def require(value, name):
    if value is None:
        raise ValueError('Value "{}" is required but missing'.format(name))
    return value


def instance_label(obj: object, label: str = '') -> str:
    return obj.__class__.__name__ + (':{}'.format(label) if label else '')


def get_logger(obj: object, label: str = '') -> logging.Logger:
    return logging.getLogger(instance_label(obj, label))
