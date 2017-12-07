import typing

from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference


class StandardResourceReference(ResourceReference):
    def __init__(self, *params):
        self._params: typing.Tuple[typing.Any] = tuple(params)  # save a copy

    def __hash__(self):
        return hash(self._params)

    def __eq__(self, other):
        # TODO needs tested
        return isinstance(other, StandardResourceReference) \
               and isinstance(other, self.__class__) \
               and (p1 == p2 for p1, p2 in zip(self.params, other.params))

    @property
    def params(self) -> typing.Iterable[typing.Any]:
        yield from self._params
