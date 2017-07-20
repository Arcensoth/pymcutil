from typing import Any, Iterable, List

from pymcutil.command.command import Command
from pymcutil.resource.abc.json_resource import JsonResource
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference
from pymcutil.resource.resource_referent.abc.resource_referent import ResourceReferent


class LootTable(JsonResource):
    def __init__(self, commands: Iterable[Command]):
        self.commands: List[Command] = list(commands)

    def serialized(self) -> Any:
        return {}  # TODO serialize loot table

    @property
    def direct_resource_references(self) -> Iterable[ResourceReference]:
        # No direct references; see entries.
        yield from ()

    @property
    def resource_referents(self) -> Iterable[ResourceReferent]:
        # Yield all loot table entries.
        yield from ()  # TODO yield loot table entries
