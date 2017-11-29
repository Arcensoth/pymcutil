import abc


class ResourceLocation(abc.ABC):
    def __str__(self):
        return self.name

    @property
    def name(self) -> str:
        return '{}:{}'.format(self.namespace, self.trail)  # TODO use utility

    @property
    @abc.abstractmethod
    def namespace(self) -> str:
        """ Return the `namespace` in `namespace:path/to/file`. """

    @property
    @abc.abstractmethod
    def trail(self) -> str:
        """ Return the `path/to/file` in `namespace:path/to/file`. """

    @property
    @abc.abstractmethod
    def path(self) -> str:
        """ Return the file path of the resource, relative to datapack root. """
