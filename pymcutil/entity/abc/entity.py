import abc
from typing import List

from pymcutil.position.position import Position
from pymcutil.position.rotation import Rotation
from pymcutil.symbols.entity_ids.entity_ids import EntityID


class Entity(abc.ABC):
    def __init__(
            self,
            pos: Position.Generic = None, motion: Position.Generic = None, rotation: Rotation.Generic = None,
            fall_distance: float = None, fire: int = None, air: int = None, on_ground: bool = None,
            no_gravity: bool = None, dimension: int = None, invulnerable: bool = None, portal_cooldown: int = None,
            uuid_most: int = None, uuid_least: int = None, custom_name: str = None, custom_name_visible: bool = None,
            silent: bool = None, passengers: List[object] = None, glowing: bool = None, tags: List[str] = None,
            **kwargs
    ):
        ...  # TODO entity attribs

    @property
    @abc.abstractmethod
    def id_(self) -> EntityID:
        """ Return the namespaced `EntityID` for this type of entity. """
