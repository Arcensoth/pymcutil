from typing import Any

from pymcutil.resource.abc.json_resource import JsonResource


class LootTable(JsonResource):
    def __init__(self, obj):
        self.obj = obj

    def serialized(self) -> Any:
        return self.obj
