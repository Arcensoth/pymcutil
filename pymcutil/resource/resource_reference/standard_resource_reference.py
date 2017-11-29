from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference


class StandardResourceReference(ResourceReference):
    def __init__(self, *params):
        super().__init__()
        self._params: tuple = tuple(params)
        self._location: ResourceLocation = None

    def locate(self, location: ResourceLocation):
        if self._location is not None:
            raise ValueError('reference cannot be located more than once')
        self._location = location

    @property
    def location(self) -> ResourceLocation:
        if self._location is None:
            raise ValueError('reference has not been located')
        return self._location

    @property
    def params(self) -> tuple:
        return self._params
