import abc
import collections
import typing

ResourceName = str
ResourcePath = str


class ResourceLocation(abc.ABC, collections.Hashable):
    @property
    @abc.abstractmethod
    def namespace(self) -> str:
        """ Return the `namespace` in `namespace:path/to/file`. """

    @property
    @abc.abstractmethod
    def components(self) -> typing.Iterable[str]:
        """ Yield the directory components of `path/to/file` in `namespace:path/to/file`. """

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
    def name(self) -> ResourceName:
        """ Return the name of the resource, to be used as a reference. """

    @property
    @abc.abstractmethod
    def path(self) -> ResourcePath:
        """ Return the file path of the resource, relative to datapack root. """
