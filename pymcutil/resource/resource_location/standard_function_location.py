from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class StandardResourceLocation(ResourceLocation):
    def __init__(self, namespace: str, trail: str, subfolder: str, extension: str = 'json'):
        self._namespace: str = namespace
        self._trail: str = trail
        self._subfolder: str = subfolder
        self._extension: str = extension

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
    def path(self) -> str:
        return 'data/{}/{}/{}.{}'.format(self.namespace, self.subfolder, self.trail, self.extension)  # TODO use utility
