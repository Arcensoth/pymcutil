import abc
from typing import Iterable, Tuple, Type

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference

ResourcePair = Tuple[Resource, ResourceLocation]


class ResourceManager(abc.ABC):
    """ Manages relationships between programmatically defined game resources for dynamic datapack generation. """

    @abc.abstractmethod
    def set_generator(self, kind: Type[ResourceReference], generator: ResourceGenerator):
        """ Set the `ResourceGenerator` for `kind` of `ResourceReference` to `generator`. """

    @abc.abstractmethod
    def get_generator(self, reference: ResourceReference) -> ResourceGenerator:
        """ Return a `ResourceGenerator` that can generate a `Resource` from the given `reference`. """

    @abc.abstractmethod
    def generate(self, *references: ResourceReference) -> Iterable[ResourcePair]:
        """ Generate `ResourcePair`s from the given `references` using `ResourceGenerator`s. """
