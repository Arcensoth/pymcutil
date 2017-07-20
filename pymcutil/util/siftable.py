import abc


class Siftable(abc.ABC):
    DEFAULT_SENTINEL = object()

    @classmethod
    def sift(cls, obj, default=DEFAULT_SENTINEL):
        if obj is None:
            if default is Siftable.DEFAULT_SENTINEL:
                raise ValueError('Cannot sift {} from nothing, with no default'.format(cls.__name__))
            obj = default

        if obj is None:
            return None

        if isinstance(obj, cls):
            return obj

        return cls._siftobj(obj)

    @classmethod
    @abc.abstractmethod
    def _siftobj(cls, obj):
        """ Return an instance of `cls` constructed from the non-`cls`, non-null generic object `obj`. """


class SiftableSequence(Siftable):
    @classmethod
    def _siftobj(cls, obj):
        return cls(*obj)


class SiftableMapping(Siftable):
    @classmethod
    def _siftobj(cls, obj):
        return cls(**obj)
