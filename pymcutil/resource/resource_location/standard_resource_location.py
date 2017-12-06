from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation, ResourceName, ResourcePath
from pymcutil.util.hash_equality import HashEquality


class StandardResourceLocation(ResourceLocation, HashEquality):
    def __init__(self, namespace: str, trail: str, subfolder: str, extension: str = 'json'):
        self._namespace: str = namespace
        self._trail: str = trail
        self._subfolder: str = subfolder
        self._extension: str = extension

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.path)

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def trail(self) -> str:
        return self._trail

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
        # TODO use utility
        return 'data/{}/{}/{}.{}'.format(self.namespace, self.subfolder, self.trail, self.extension)