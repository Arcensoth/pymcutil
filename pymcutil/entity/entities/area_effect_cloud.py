from pymcutil.entity.abc.entity import Entity
from pymcutil.symbols import entity_ids
from pymcutil.symbols.entity_ids.entity_ids import EntityID


class AreaEffectCloud(Entity):
    def __init__(
            self,
            age: int = None, color: int = None, duration: int = None, reapplication_delay: int = None,
            wait_time: int = None, owner_uuid_least: int = None, owner_uuid_most: int = None,
            duration_on_use: float = None, radius: float = None, radius_on_use: float = None,
            radius_per_tick: float = None, particle: str = None,
            particle_param_1: int = None, particle_param_2: int = None, potion: str = None,
            effects: list = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        # TODO area effect cloud attribs

    @property
    def id_(self) -> EntityID:
        return entity_ids.area_effect_cloud
