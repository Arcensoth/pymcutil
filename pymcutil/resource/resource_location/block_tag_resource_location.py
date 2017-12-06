import typing

from pymcutil.resource.resource_location.tag_resource_location import TagResourceLocation


class BlockTagResourceLocation(TagResourceLocation):
    def __init__(self, namespace: str, components: typing.Iterable[str]):
        super().__init__(namespace=namespace, components=('blocks', *components))
