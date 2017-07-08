import abc
from typing import Iterable

from pymcutil.resource.resource_referent.abc.resource_referent import ResourceReferent


class Resource(ResourceReferent):
    """ Generic game resource representation, used to define common access methods. """

    @property
    @abc.abstractmethod
    def resource_lines(self) -> Iterable:
        """ Yield lines to be written to the resource file. """
