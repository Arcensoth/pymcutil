import abc


class Resource(abc.ABC):
    """ Generic game resource representation, used to define common access methods. """

    @abc.abstractmethod
    def write_to(self, path):
        """ Write this `Resource` to file at `path`. """
