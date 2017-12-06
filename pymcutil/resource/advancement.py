from typing import Any

from pymcutil.resource.abc.json_resource import JsonResource


class Advancement(JsonResource):
    def __init__(self, obj: dict):
        self.obj: dict = obj

    def serialized(self) -> Any:
        return self.obj
