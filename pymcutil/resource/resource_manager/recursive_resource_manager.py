import logging
import os
from typing import Dict, Iterable, Mapping, Type

from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager, ResourcePair
from pymcutil.resource.resource_manager.errors import ResourceReferenceNotMappedError
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference

log = logging.getLogger('rm')


class RecursiveResourceManager(ResourceManager):
    def __init__(self, mapping: Mapping, output_root: str):
        self.mapping: Dict[Type[ResourceReference], ResourceGenerator] = dict(mapping)
        self.output_root: str = output_root

    def _locate(self, reference: ResourceReference):
        generator = self.get_generator(reference)
        location = generator.location(*reference.params)
        reference.locate(location)

    def set_generator(self, kind: Type[ResourceReference], generator: ResourceGenerator):
        self.mapping[kind] = generator

    def get_generator(self, reference: ResourceReference) -> ResourceGenerator:
        try:
            return self.mapping[type(reference)]
        except KeyError:
            raise ResourceReferenceNotMappedError(reference)

    def rgenerate(self, reference: ResourceReference) -> Iterable[ResourcePair]:
        generator = self.get_generator(reference)
        resource = generator.generate(*reference.params)

        log.info('Recursively generating resource: {}'.format(reference.location.name))

        # Locate dependencies before generating output.
        for subref in resource.resource_references:
            self._locate(subref)

        yield resource, reference.location

        # TODO refactor duplicate code
        resource_path = os.path.join(self.output_root, reference.location.path)
        os.makedirs(os.path.dirname(resource_path), exist_ok=True)
        with open(resource_path, 'w') as resource_file:
            resource_file.write(resource.text)

        # Recursively generate dependencies.
        for subref in resource.resource_references:
            yield from self.rgenerate(subref)

    def generate(self, *references: ResourceReference) -> Iterable[ResourcePair]:
        for ref in references:
            self._locate(ref)
            yield from self.rgenerate(ref)
