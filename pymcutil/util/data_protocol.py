import collections


class DataProtocol(collections.Iterable):
    def __init__(self, **kwargs):
        self._data: dict = {}
        for k, v in kwargs.items():
            if v is not None:
                setattr(self, k, v)

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __len__(self):
        return self._data.__len__()

    def __iter__(self):
        return self._data.items()

    def _get(self, name: str):
        return self._data.get(name)

    def _set(self, name: str, value, type_: type):
        assert isinstance(value, type_)
        self._data[name] = value

    def _del(self, name: str):
        del self._data[name]
