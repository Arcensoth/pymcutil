import typing

from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation, ResourceName, ResourcePath


class StandardResourceLocation(ResourceLocation):
    def __init__(self, namespace: str, components: typing.Iterable[str], subfolder: str, extension: str = 'json'):
        self._namespace: str = namespace
        self._components: typing.Tuple[str] = tuple(components)  # save a copy
        self._subfolder: str = subfolder
        self._extension: str = extension

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, other):
        return isinstance(other, StandardResourceLocation) \
               and isinstance(other, self.__class__) \
               and (self.path == other.path)

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def components(self) -> typing.Iterable[str]:
        yield from self._components

    @property
    def trail(self) -> str:
        # TODO use utility
        return '/'.join(self.components)

    @property
    def subfolder(self) -> str:
        return self._subfolder

    @property
    def extension(self) -> str:
        return self._extension

    @property
    def name(self) -> ResourceName:
        # TODO use utility
        return '{}:{}'.format(self.namespace, self.trail)

    @property
    def path(self) -> ResourcePath:
        # TODO use utility with os-specific separator
        return 'data/{}/{}/{}.{}'.format(self.namespace, self.subfolder, self.trail, self.extension)
