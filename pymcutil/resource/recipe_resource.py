from typing import Any

from pymcutil.resource.abc.json_resource import JsonResource


class RecipeResource(JsonResource):
    def __init__(self, obj: dict):
        self.obj: dict = obj

    def serialized(self) -> Any:
        return self.obj
