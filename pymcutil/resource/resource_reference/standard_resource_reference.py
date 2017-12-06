import typing

from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference
from pymcutil.util.hash_equality import HashEquality


class StandardResourceReference(ResourceReference, HashEquality):
    def __init__(self, *params):
        self._params: typing.Tuple[typing.Any] = tuple(params)  # save a copy

    def __hash__(self):
        return hash(self._params)

    @property
    def params(self) -> typing.Iterable[typing.Any]:
        yield from self._params
