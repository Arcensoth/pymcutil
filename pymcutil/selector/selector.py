import abc
from numbers import Real
from typing import Iterable, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.repeatable_argument import RepeatableArgument
from pymcutil.selector.score_set import ScoreSet
from pymcutil.symbols.gamemodes.gamemode import Gamemode
from pymcutil.symbols.selector_sorts.selector_sort import SelectorSort
from pymcutil.util import first
from pymcutil.util.common_mapping import CommonMapping

RepeatableString = Union[str, Iterable[str]]
RepeatableGamemode = Union[Gamemode, Iterable[Gamemode]]
RepeatableNBT = Union[CompoundDataTag.Generic, Iterable[CompoundDataTag.Generic]]


class Selector(CommonMapping):
    """
    Represents a Minecraft target selector, with similar arguments and some built-in conveniences.

    Provided arguments cascade such that the most specific value is used. For example, an explicitly provided `x`
    coordinate will take precedence over the `x` component of any given `position`.
    """

    def __init__(
            self,
            position: Position.Generic = None, x: Real = None, y: Real = None, z: Real = None,
            volume: Position.Generic = None, dx: Real = None, dy: Real = None, dz: Real = None,
            x_rotation: Range.Generic = None, y_rotation: Range.Generic = None,
            distance: Range.Generic = None,
            level: Range.Generic = None,
            type_: str = None, not_types: RepeatableString = None,
            name: str = None, not_names: RepeatableString = None,
            team: str = None, not_teams: RepeatableString = None,
            gamemode: Gamemode = None, not_gamemodes: RepeatableGamemode = None,
            tags: RepeatableString = None, not_tags: RepeatableString = None,
            nbts: RepeatableNBT = None, not_nbts: RepeatableNBT = None,
            scores: ScoreSet.Generic = None,
            advancements: AdvancementSet.Generic = None,
            sort: SelectorSort = None,
            limit: int = None,
    ):
        # Don't actually save these; just use them for intermediate calculations.
        position = Position.sift(position, None)
        volume = Position.sift(volume, None)

        # Build an initial mapping of arguments.
        mapping = dict(
            x=first(x, position.x if isinstance(position, Position) else None),
            y=first(y, position.y if isinstance(position, Position) else None),
            z=first(z, position.z if isinstance(position, Position) else None),

            dx=first(dx, volume.x if isinstance(volume, Position) else None),
            dy=first(dy, volume.y if isinstance(volume, Position) else None),
            dz=first(dz, volume.z if isinstance(volume, Position) else None),

            x_rotation=Range.sift(x_rotation, None),
            y_rotation=Range.sift(y_rotation, None),

            distance=Range.sift(distance, None),

            level=Range.sift(level, None),

            type=type_,
            not_types=RepeatableArgument.expand(not_types),

            name=name,
            not_names=RepeatableArgument.expand(not_names),

            team=team,
            not_teams=RepeatableArgument.expand(not_teams),

            gamemode=gamemode,
            not_gamemodes=RepeatableArgument.expand(not_gamemodes, converter=Gamemode.sift),

            tags=RepeatableArgument.expand(tags),
            not_tags=RepeatableArgument.expand(not_tags),

            nbts=RepeatableArgument.expand(nbts, CompoundDataTag.sift),
            not_nbts=RepeatableArgument.expand(not_nbts, CompoundDataTag.sift),

            scores=ScoreSet.sift(scores, None),

            advancements=AdvancementSet.sift(advancements, None),

            sort=SelectorSort.sift(sort, None),

            limit=limit,
        )

        # Remove null values from the mapping before using it.
        culled_mapping = {k: v for k, v in mapping.items() if v is not None}

        super().__init__(**culled_mapping)

    def __str__(self):
        innards = ','.join(('{}={}'.format(k, v) for k, v in self.expanded_items()))
        return ''.join((
            '@',
            self.base,
            *(('[', innards, ']') if innards else ()),
        ))

    def expanded_items(self):
        # We need to expand `RepeatableArguments` to get several items per key.
        for k, v in self.items():
            if isinstance(v, RepeatableArgument):
                yield from (k, rv for rv in v.values)
            else:
                yield k, v

    @property
    def x(self) -> Union[Real, None]:
        return self.get('x', None)

    @property
    def y(self) -> Union[Real, None]:
        return self.get('y', None)

    @property
    def z(self) -> Union[Real, None]:
        return self.get('z', None)

    @property
    def dx(self) -> Union[Real, None]:
        return self.get('dx', None)

    @property
    def dy(self) -> Union[Real, None]:
        return self.get('dy', None)

    @property
    def dz(self) -> Union[Real, None]:
        return self.get('dz', None)

    @property
    def distance(self) -> Union[Range, None]:
        return self.get('distance', None)

    @property
    def level(self) -> Union[Range, None]:
        return self.get('level', None)

    @property
    def x_rotation(self) -> Union[Range, None]:
        return self.get('x_rotation', None)

    @property
    def y_rotation(self) -> Union[Range, None]:
        return self.get('y_rotation', None)

    @property
    def type(self) -> Union[str, None]:
        return self.get('type', None)

    @property
    def not_types(self) -> Union[RepeatableArgument[str], None]:
        return self.get('not_types', None)

    @property
    def name(self) -> Union[str, None]:
        return self.get('name', None)

    @property
    def not_names(self) -> Union[RepeatableArgument[str], None]:
        return self.get('not_names', None)

    @property
    def team(self) -> Union[str, None]:
        return self.get('team', None)

    @property
    def not_teams(self) -> Union[RepeatableArgument[str], None]:
        return self.get('not_teams', None)

    @property
    def gamemode(self) -> Union[Gamemode, None]:
        return self.get('gamemode', None)

    @property
    def not_gamemodes(self) -> Union[RepeatableArgument[Gamemode], None]:
        return self.get('not_gamemodes', None)

    @property
    def tags(self) -> Union[RepeatableArgument[str], None]:
        return self.get('tags', None)

    @property
    def not_tags(self) -> Union[RepeatableArgument[str], None]:
        return self.get('not_tags', None)

    @property
    def nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self.get('nbts', None)

    @property
    def not_nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self.get('not_nbts', None)

    @property
    def scores(self) -> Union[ScoreSet, None]:
        return self.get('scores', None)

    @property
    def advancements(self) -> Union[AdvancementSet, None]:
        return self.get('advancements', None)

    @property
    def sort(self) -> Union[SelectorSort, None]:
        return self.get('sort', None)

    @property
    def limit(self) -> Union[int, None]:
        return self.get('limit', None)

    @classmethod
    @abc.abstractmethod
    def base(cls) -> str:
        """ Return the base selector type. For example, the `s` in `@s`. """
