import typing
from numbers import Real

from pymcutil.position.position import Position
from pymcutil.position.rotation import Rotation
from pymcutil.util.data_map import DataMap


class EntityData(DataMap):
    # TODO passengers type needs recursive reference
    def __init__(
            self,
            pos: Position = None, motion: Position = None, rotation: Rotation = None, fall_distance: Real = None,
            fire: int = None, air: int = None, on_ground: bool = None, no_gravity: bool = None, dimension: int = None,
            invulnerable: bool = None, portal_cooldown: int = None, uuid_most: int = None, uuid_least: int = None,
            custom_name: str = None, custom_name_visible: bool = None, silent: bool = None,
            passengers: typing.List[object] = None, glowing: bool = None, tags: typing.List[str] = None,
            **kwargs
    ):
        super().__init__(
            pos=pos, motion=motion, rotation=rotation, fall_distance=fall_distance, fire=fire, air=air,
            on_ground=on_ground, no_gravity=no_gravity, dimension=dimension, invulnerable=invulnerable,
            portal_cooldown=portal_cooldown, uuid_most=uuid_most, uuid_least=uuid_least, custom_name=custom_name,
            custom_name_visible=custom_name_visible, silent=silent, passengers=passengers, glowing=glowing, tags=tags,
            **kwargs
        )

    # TODO properties
