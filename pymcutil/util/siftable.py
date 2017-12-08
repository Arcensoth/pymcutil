import abc


class Siftable(abc.ABC):
    DEFAULT_SENTINEL = object()

    @classmethod
    def sift(cls, obj, default=DEFAULT_SENTINEL):
        # If a value was not supplied, try the default.
        if obj is None:
            if default is cls.DEFAULT_SENTINEL:
                raise ValueError('Cannot create {} from nothing, with no default'.format(cls.__name__))
            obj = default

        # If the value explicitly defaulted to null, just return the same.
        if obj is None:
            return None

        # If the value is already an instance of this same class, just return it as is.
        if isinstance(obj, cls):
            return obj

        # Finally, trying converting the value into an instance of this class.
        converted = cls._from_other(obj)
        if converted is not None:
            return converted

        raise ValueError('Cannot convert {} to {}'.format(obj.__class__.__name__, cls.__name__))

    @classmethod
    @abc.abstractmethod
    def _from_other(cls, obj):
        """ Return an instance of `cls` constructed from the non-`cls`, non-null generic object `obj`. """


class SequenceSiftable(Siftable):
    @classmethod
    def _from_other(cls, obj):
        return cls(*obj)


class MappingSiftable(Siftable):
    @classmethod
    def _from_other(cls, obj):
        return cls(**obj)
