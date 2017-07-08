from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class FunctionLocation(ResourceLocation):
    def __init__(self, namespace: str, trail: str):
        self._namespace: str = namespace
        self._trail: str = trail

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def trail(self) -> str:
        return self._trail

    @property
    def path(self) -> str:
        return 'data/{}/functions/{}.mcfunction'.format(self.namespace, self.trail)  # TODO use utility
