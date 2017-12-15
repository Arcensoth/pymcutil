from pymcutil.entity.entity_data import EntityData


class AreaEffectCloudData(EntityData):
    # TODO effects type needs EffectData reference
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
        super().__init__(
            age=age, color=color, duration=duration, reapplication_delay=reapplication_delay, wait_time=wait_time,
            owner_uuid_least=owner_uuid_least, owner_uuid_most=owner_uuid_most, duration_on_use=duration_on_use,
            radius=radius, radius_on_use=radius_on_use, radius_per_tick=radius_per_tick, particle=particle,
            particle_param_1=particle_param_1, particle_param_2=particle_param_2, potion=potion, effects=effects,
            **kwargs
        )

    # TODO properties
