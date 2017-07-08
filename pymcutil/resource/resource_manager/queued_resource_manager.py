import os
from queue import Queue
from typing import Dict, Iterable, Mapping, Type

from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager, ResourcePair
from pymcutil.resource.resource_manager.errors import ResourceReferenceNotMappedError
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference


class QueuedResourceManager(ResourceManager):
    def __init__(self, mapping: Mapping, output_root: str):
        self.mapping: Dict[Type[ResourceReference], ResourceGenerator] = dict(mapping)
        self.output_root: str = output_root

    def set_generator(self, kind: Type[ResourceReference], generator: ResourceGenerator):
        self.mapping[kind] = generator

    def get_generator(self, reference: ResourceReference) -> ResourceGenerator:
        try:
            return self.mapping[type(reference)]
        except KeyError:
            raise ResourceReferenceNotMappedError(reference)

    def locate(self, reference: ResourceReference):
        generator = self.get_generator(reference)
        location = generator.location(*reference.params)
        reference.locate(location)

    def generate(self, *references: ResourceReference) -> Iterable[ResourcePair]:
        q: Queue = Queue()

        # Locate seed refs before anything else.
        for ref in references:
            self.locate(ref)
            q.put(ref)

        while not q.empty():
            resource_reference: ResourceReference = q.get()
            generator = self.get_generator(resource_reference)
            resource = generator.generate(*resource_reference.params)

            # Locate dependencies before generating output.
            for subref in resource.resource_references:
                self.locate(subref)
                q.put(subref)

            resource_location = resource_reference.location
            resource_path = os.path.join(self.output_root, resource_location.path)

            os.makedirs(os.path.dirname(resource_path), exist_ok=True)

            with open(resource_path, 'w') as resource_file:
                resource_file.write('\n'.join([str(line) for line in resource.resource_lines] + ['']))

            yield resource, resource_location
