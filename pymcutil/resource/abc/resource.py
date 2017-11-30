import abc


class Resource(object):
    """ Generic game resource representation, used to define common access methods. """

    @property
    @abc.abstractmethod
    def text(self) -> str:
        """ Return the string version of the resource to be written to file. """
