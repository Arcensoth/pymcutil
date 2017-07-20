import os
from typing import Dict, Iterable, Mapping, Type

from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager, ResourcePair
from pymcutil.resource.resource_manager.errors import ResourceReferenceNotMappedError
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference
from pymcutil.util.stack import Stack


class StackedResourceManager(ResourceManager):
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

    def generate(self, *references: ResourceReference) -> Iterable[ResourcePair]:
        stack: Stack = Stack()

        # Locate seed refs before anything else.
        for ref in reversed(references):
            self._locate(ref)
            stack.push(ref)

        while not stack.empty():
            reference: ResourceReference = stack.pop()
            generator = self.get_generator(reference)
            resource = generator.generate(*reference.params)

            # Reverse the order in which we push dependencies, so that the next item popped after this iteration is the
            # first dependency that was encountered.
            reversed_refs = reversed(list(resource.resource_references))

            # Locate dependencies before generating output.
            for subref in reversed_refs:
                self._locate(subref)
                stack.push(subref)

            yield resource, reference.location

            # TODO refactor duplicate code
            resource_path = os.path.join(self.output_root, reference.location.path)
            os.makedirs(os.path.dirname(resource_path), exist_ok=True)
            with open(resource_path, 'w') as resource_file:
                resource_file.write(resource.text)
