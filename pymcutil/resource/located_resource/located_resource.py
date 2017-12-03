from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class LocatedResource(object):
    """ Uses components to pair a `ResourceLocation` with a `Resource`. """

    def __init__(self, location: ResourceLocation, resource: Resource):
        self.location: ResourceLocation = location
        self.resource: Resource = resource
