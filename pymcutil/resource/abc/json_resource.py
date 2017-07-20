import json

from pymcutil.resource.abc.resource import Resource
from pymcutil.util.serializable import Serializable


class JsonResource(Resource, Serializable):
    @property
    def text(self) -> str:
        return json.dumps(self.serialized, sort_keys=True, indent=4)
