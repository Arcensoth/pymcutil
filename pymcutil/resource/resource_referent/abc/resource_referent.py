import abc
from typing import Iterable

from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference


class ResourceReferent(abc.ABC):
    @property
    def resource_references(self) -> Iterable[ResourceReference]:
        yield from self.direct_resource_references
        for referent in self.resource_referents:
            yield from referent.resource_references

    @property
    @abc.abstractmethod
    def direct_resource_references(self) -> Iterable[ResourceReference]:
        """ Yield `ResourceReference`s for any managed resources that are *directly* referenced by this object. All
        indirect (recursive) references should be handled by `ResourceReferent.referents()` instead."""

    @property
    @abc.abstractmethod
    def resource_referents(self) -> Iterable['ResourceReferent']:
        """ Yield any `ResourceReferent`s within this object, resulting in recursive referencing. """
