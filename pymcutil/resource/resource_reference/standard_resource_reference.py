from typing import Tuple

from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference
from pymcutil.util.hash_equality import HashEquality


class StandardResourceReference(ResourceReference, HashEquality):
    def __init__(self, *params):
        super().__init__()
        self._params: Tuple = tuple(params)

    def __hash__(self):
        return hash(self.params)

    @property
    def params(self) -> Tuple:
        return self._params
