import collections


class DataMap(collections.MutableMapping):
    def __init__(self, **kwargs):
        self._data: dict = {}
        for k, v in kwargs.items():
            if v is not None:
                setattr(self, k, v)

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __delitem__(self, key):
        return self._data.__delitem__(key)

    def __len__(self):
        return self._data.__len__()

    def __iter__(self):
        return self._data.__iter__()

    def _get(self, name: str):
        return self._data.get(name)

    def _set(self, name: str, value: object, type_: type):
        if not isinstance(value, type_):
            raise ValueError('Property "{}" must be type "{}", but got "{}"'.format(
                name, type_.__name__, value.__class__.__name__))
        self._data[name] = value

    def _del(self, name: str):
        del self._data[name]
