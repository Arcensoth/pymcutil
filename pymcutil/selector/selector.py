import abc
from numbers import Real
from typing import Any, Iterable, Iterator, Tuple, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.score_set import ScoreSet
from pymcutil.selector.selector_sort import SelectorSort
from pymcutil.util import first
from pymcutil.util.gamemode import Gamemode

RepeatableString = Union[str, Iterable[str]]
RepeatableGamemode = Union[Gamemode, Iterable[Gamemode]]
RepeatableNBT = Union[CompoundDataTag.Generic, Iterable[CompoundDataTag.Generic]]


def tuplize(obj) -> tuple:
    if obj is None:
        return ()
    elif isinstance(obj, (str, Gamemode, CompoundDataTag.Generic)):
        return obj,  # wrap in a tuple
    elif isinstance(obj, Iterable):
        return tuple(obj)  # make a copy
    raise ValueError('Invalid selector argument: {}'.format(obj))


class Selector(abc.ABC):
    """
    Represents a Minecraft target selector, with similar arguments and some built-in conveniences.

    Provided arguments cascade such that the most specific value is used. For example, an explicitly provided `x`
    coordinate will take precedence over the `x` component of any given `position`.
    """

    def __init__(
            self,
            position: Position.Generic = None, x: Real = None, y: Real = None, z: Real = None,
            volume: Position.Generic = None, dx: Real = None, dy: Real = None, dz: Real = None,
            distance: Range.Generic = None, level: Range.Generic = None,
            x_rotation: Range.Generic = None, y_rotation: Range.Generic = None,
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
        self._position: Position = Position.sift(position, None)
        self._x: Real = x
        self._y: Real = y
        self._z: Real = z

        self._volume: Position = Position.sift(volume, None)
        self._dx: Real = dx
        self._dy: Real = dy
        self._dz: Real = dz

        self._distance: Range = distance
        self._level: Range = level

        self._x_rotation: Range = x_rotation
        self._y_rotation: Range = y_rotation

        self._type: str = type_
        self._not_types: Tuple[str] = tuplize(not_types)

        self._name: str = name
        self._not_names: Tuple[str] = tuplize(not_names)

        self._team: str = team
        self._not_teams: Tuple[str] = tuplize(not_teams)

        self._gamemode: Gamemode = gamemode
        self._not_gamemodes: Tuple[Gamemode] = tuplize(not_gamemodes)

        self._tags: Tuple[str] = tuplize(tags)
        self._not_tags: Tuple[str] = tuplize(not_tags)

        # Note that `nbt` is a tuple of DataTag objects, not itself a DataTag.
        self._nbts: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(nbts)) if nbts else ()
        self._not_nbts: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(not_nbts)) if not_nbts else ()

        self._scores: ScoreSet = ScoreSet.sift(scores, None)

        self._advancements: AdvancementSet = AdvancementSet.sift(advancements, None)

        self._sort: SelectorSort = sort

        self._limit: int = limit

    def __str__(self):
        return self.to_str()

    def _arguments_nullable(self):
        yield 'x=', self.x
        yield 'y=', self.y
        yield 'z=', self.z

        yield 'dx=', self.dx
        yield 'dy=', self.dy
        yield 'dz=', self.dz

        yield 'distance=', self.distance
        yield 'level=', self.level

        yield 'x_rotation=', self.x_rotation
        yield 'y_rotation=', self.y_rotation

        yield 'type=', self.type
        yield from (('type=!', type_) for type_ in self.not_types)

        # TODO sanitize name and tags in case of spaces

        yield 'name=', self.name
        yield from (('name=!', name) for name in self.not_names)

        yield 'team=', self.team
        yield from (('team=!', team) for team in self.not_teams)

        yield 'gamemode=', self.gamemode
        yield from (('gamemode=!', gamemode) for gamemode in self.not_gamemodes)

        yield from (('tag=', tag) for tag in self.tags)
        yield from (('tag=!', tag) for tag in self.not_tags)

        yield from (('nbt=', nbt) for nbt in self.nbts)
        yield from (('nbt=!', nbt) for nbt in self.not_nbts)

        yield 'scores=', self.scores

        yield 'advancements=', self.advancements

        yield 'sort=', self.sort

        yield 'limit=', self.limit

    def _arguments(self) -> Iterator[Tuple[str, Any]]:
        yield from ((k, v) for k, v in self._arguments_nullable() if v is not None)

    @property
    def x(self) -> Real:
        return first(self._x, self._position.x if self._position is not None else None)

    @property
    def y(self) -> Real:
        return first(self._y, self._position.y if self._position is not None else None)

    @property
    def z(self) -> Real:
        return first(self._z, self._position.z if self._position is not None else None)

    @property
    def dx(self) -> Real:
        return first(self._dx, self._volume.x if self._volume is not None else None)

    @property
    def dy(self) -> Real:
        return first(self._dy, self._volume.y if self._volume is not None else None)

    @property
    def dz(self) -> Real:
        return first(self._dz, self._volume.z if self._volume is not None else None)

    @property
    def distance(self) -> Range:
        return self._distance

    @property
    def level(self) -> Range:
        return self._level

    @property
    def x_rotation(self) -> Range:
        return self._x_rotation

    @property
    def y_rotation(self) -> Range:
        return self._y_rotation

    @property
    def type(self) -> str:
        return self._type

    @property
    def not_types(self) -> Tuple[str]:
        return self._not_types

    @property
    def name(self) -> str:
        return self._name

    @property
    def not_names(self) -> Tuple[str]:
        return self._not_names

    @property
    def team(self) -> str:
        return self._team

    @property
    def not_teams(self) -> Tuple[str]:
        return self._not_teams

    @property
    def gamemode(self) -> Gamemode:
        return self._gamemode

    @property
    def not_gamemodes(self) -> Tuple[Gamemode]:
        return self._not_gamemodes

    @property
    def tags(self) -> Tuple[str]:
        return self._tags

    @property
    def not_tags(self) -> Tuple[str]:
        return self._not_tags

    @property
    def nbts(self) -> Tuple[CompoundDataTag]:
        return self._nbts

    @property
    def not_nbts(self) -> Tuple[CompoundDataTag]:
        return self._not_nbts

    @property
    def scores(self) -> ScoreSet:
        return self._scores

    @property
    def advancements(self) -> AdvancementSet:
        return self._advancements

    @property
    def sort(self) -> SelectorSort:
        return self._sort

    @property
    def limit(self) -> int:
        return self._limit

    def to_str(self) -> str:
        selector_str = '@{}'.format(self.base)
        args_str = ','.join('='.join((key, str(value))) for key, value in self._arguments())
        if args_str:
            selector_str = '{}[{}]'.format(selector_str, args_str)
        return selector_str

    @property
    @abc.abstractmethod
    def base(self) -> str:
        """ Return the base selector type. """
