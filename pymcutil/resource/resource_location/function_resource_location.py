import typing

from pymcutil.resource.resource_location.standard_resource_location import StandardResourceLocation


class FunctionResourceLocation(StandardResourceLocation):
    def __init__(self, namespace: str, components: typing.Iterable[str]):
        super().__init__(namespace=namespace, components=components, subfolder='functions', extension='mcfunction')
