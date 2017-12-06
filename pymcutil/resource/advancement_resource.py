from typing import Any

from pymcutil.resource.abc.json_resource import JsonResource


class AdvancementResource(JsonResource):
    def __init__(self, obj: dict):
        self.obj: dict = obj

    @property
    def serialized(self) -> Any:
        return self.obj
