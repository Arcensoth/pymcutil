from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_manager.errors import ReferenceNotRegisteredError, ResourceDidNotGenerateError


class StandardResourceManager(ResourceManager):
    def __init__(self, database, registry):
        self._database = database

        self._generator_map = {}
        self._database_map = {}

        self._generating = set()

        for item in registry:
            self.register(*item)

    def _get_generator(self, reference):
        try:
            return self._generator_map[type(reference)]
        except KeyError as e:
            raise ReferenceNotRegisteredError(reference) from e

    def _get_database(self, reference):
        return self._database_map.get(type(reference), self._database)

    def register(self, kind, generator, database=None):
        self._generator_map[kind] = generator
        self._database_map[kind] = database or self._database

    def get(self, reference):
        generator = self._get_generator(reference)
        database = self._get_database(reference)
        location = generator.location(self, reference)
        resource = database.get(location)
        return resource

    def generate(self, reference):
        self.locate(reference)
        resource = self.get(reference)
        if not resource:
            raise ResourceDidNotGenerateError(reference)
        return resource

    def locate(self, reference):
        located_resource = self.get(reference)

        if located_resource:
            location = located_resource.location

        else:
            generator = self._get_generator(reference)
            location = generator.location(self, reference)

            # Avoid deadlocks due to circular references.
            if reference not in self._generating:
                self._generating.add(reference)

                database = self._get_database(reference)
                resource = generator.generate(self, reference)
                database.put(location, resource)

                self._generating.remove(reference)

        return location

    def name(self, reference):
        return self.locate(reference).name

    def path(self, reference):
        return self.locate(reference).path
