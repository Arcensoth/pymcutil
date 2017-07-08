import os
from queue import Queue
from typing import Dict, Iterable, Mapping, Tuple, Type

from pymcutil import util
from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation
from pymcutil.resource.resource_manager.errors import ResourceReferenceNotMappedError
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference

ResourcePair = Tuple[Resource, ResourceLocation]


class ResourceManager(object):
    """ Manages relationships between programmatically defined game resources for dynamic datapack generation. """

    def __init__(self, mapping: Mapping, output_root: str, label: str = ''):
        self.mapping: Dict[Type[ResourceReference], ResourceGenerator] = dict(mapping)
        self.output_root: str = output_root

        self.label: str = label
        self.log = util.get_logger(self, self.label)

    def log_resources(self, resource_pairs: Iterable[ResourcePair]):
        resource_pairs = tuple(resource_pairs)

        self.log.info(' Generated {} resources:'.format(len(resource_pairs)))

        for resource, resource_location in resource_pairs[:-1]:
            self.log.info(' ├ {} ({})'.format(resource_location.name, resource_location.path))
            resource_lines = tuple(resource.resource_lines)
            for line in resource_lines[:-1]:
                self.log.debug('│ ├ {}'.format(line))
            last_line = resource_lines[-1:][0]
            self.log.debug('│ └ {}'.format(last_line))

        last_resource, last_resource_location = resource_pairs[-1:][0]
        self.log.info(' └ {} ({})'.format(last_resource_location.name, last_resource_location.path))
        last_resource_lines = tuple(last_resource.resource_lines)
        for line in last_resource_lines[:-1]:
            self.log.debug('  ├ {}'.format(line))
        last_resource_line = last_resource_lines[-1:][0]
        self.log.debug('  └ {}'.format(last_resource_line))

    def map(self, kind: Type[ResourceReference], generator: ResourceGenerator):
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

    def generate(self, *seed_references: ResourceReference) -> Iterable[ResourcePair]:
        q: Queue = Queue()

        # Locate seed refs before anything else.
        for ref in seed_references:
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
