class RC(float):
    """ A float wrapper for dealing with relative coordinates. """

    def __repr__(self):
        return '{name}({params})'.format(
            name=self.__class__.__name__,
            params=super().__repr__())

    def __str__(self):
        return '~' + (super().__str__() if self else '')

    def __eq__(self, other):
        if type(other) is type(self):
            return super().__eq__(other)
        return False

    def __add__(self, other):
        try:
            return RC(super().__add__(other))
        except Exception as e:
            raise TypeError('{self!r} cannot add with {other!r}'.format(self=self, other=other)) from e

    def __sub__(self, other):
        try:
            return RC(super().__sub__(other))
        except Exception as e:
            raise TypeError('{self!r} cannot sub with {other!r}'.format(self=self, other=other)) from e

    def __mul__(self, other):
        try:
            return RC(super().__mul__(other))
        except Exception as e:
            raise TypeError('{self!r} cannot mul with {other!r}'.format(self=self, other=other)) from e

    def __truediv__(self, other):
        try:
            return RC(super().__truediv__(other))
        except Exception as e:
            raise TypeError('{self!r} cannot truediv with {other!r}'.format(self=self, other=other)) from e

    def __floordiv__(self, other):
        try:
            return RC(super().__floordiv__(other))
        except Exception as e:
            raise TypeError('{self!r} cannot floordiv with {other!r}'.format(self=self, other=other)) from e

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __format__(self, format_spec):
        return '~' + (super().__format__(format_spec) if self else '')


def rel(value):
    """ Shortcut method for creating individual relative coordinates. """
    return RC(value)
