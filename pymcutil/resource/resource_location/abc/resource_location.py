import abc

ResourceName = str


class ResourceLocation(abc.ABC):
    def __str__(self):
        return self.name

    @property
    def name(self) -> ResourceName:
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
    def subfolder(self) -> str:
        """ Return the datapack subfolder where the resource should reside. """

    @property
    @abc.abstractmethod
    def extension(self) -> str:
        """ Return the file extension of the resource. """

    @property
    @abc.abstractmethod
    def path(self) -> str:
        """ Return the file path of the resource, relative to datapack root. """
