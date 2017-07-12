import json
from typing import Iterable

from pymcutil.resource.abc.resource import Resource
from pymcutil.util.serializable import Serializable


class JsonResource(Resource, Serializable):
    @property
    def resource_lines(self) -> Iterable:
        s = json.dumps(self.serialized, sort_keys=True, indent=4)  # TODO make optional
        yield from s.splitlines()
