import json

from pymcutil.resource.abc.resource import Resource
from pymcutil.util.serializable import Serializable


class JsonResource(Resource, Serializable):
    def write_to(self, path):
        with open(path, 'w') as fp:
            json.dump(self.serialized, fp, sort_keys=True, indent=2)
