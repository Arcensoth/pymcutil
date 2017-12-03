import abc


class ResourceManager(abc.ABC):
    @abc.abstractmethod
    def register(self, kind, generator, database=None): ...

    @abc.abstractmethod
    def get(self, reference): ...

    @abc.abstractmethod
    def generate(self, reference): ...

    @abc.abstractmethod
    def locate(self, reference): ...

    @abc.abstractmethod
    def name(self, reference): ...

    @abc.abstractmethod
    def path(self, reference): ...
