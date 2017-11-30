from typing import Tuple

from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference


class StandardResourceReference(ResourceReference):
    def __init__(self, *params):
        super().__init__()
        self._params: Tuple = tuple(params)

    @property
    def params(self) -> Tuple:
        return self._params
