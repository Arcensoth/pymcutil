from numbers import Real
from typing import Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.repeatable_argument import RepeatableArgument
from pymcutil.selector.score_set import ScoreSet
from pymcutil.symbols.gamemodes.gamemode import Gamemode
from pymcutil.symbols.selector_sorts.selector_sort import SelectorSort
from pymcutil.util.data_protocol import DataProtocol


class SelectorArguments(DataProtocol):
    def __init__(
            self,
            x: Real = None, y: Real = None, z: Real = None,
            dx: Real = None, dy: Real = None, dz: Real = None,
            x_rotation: Range = None, y_rotation: Range = None,
            distance: Range = None,
            level: Range = None,
            type_: str = None, not_types: RepeatableArgument[str] = None,
            name: str = None, not_names: RepeatableArgument[str] = None,
            team: str = None, not_teams: RepeatableArgument[str] = None,
            gamemode: Gamemode = None, not_gamemodes: RepeatableArgument[Gamemode] = None,
            tags: RepeatableArgument[str] = None, not_tags: RepeatableArgument[str] = None,
            nbts: RepeatableArgument[CompoundDataTag] = None, not_nbts: RepeatableArgument[CompoundDataTag] = None,
            scores: ScoreSet = None,
            advancements: AdvancementSet = None,
            sort: SelectorSort = None,
            limit: int = None,
    ):
        super().__init__(
            x=x, y=y, z=z, dx=dx, dy=dy, dz=dz, x_rotation=x_rotation, y_rotation=y_rotation, distance=distance,
            level=level, type_=type_, not_types=not_types, name=name, not_names=not_names, team=team,
            not_teams=not_teams, gamemode=gamemode, not_gamemodes=not_gamemodes, tags=tags, not_tags=not_tags,
            nbts=nbts, not_nbts=not_nbts, scores=scores, advancements=advancements, sort=sort, limit=limit)

    @property
    def x(self) -> Union[Real, None]:
        return self._get('x')

    @property
    def y(self) -> Union[Real, None]:
        return self._get('y')

    @property
    def z(self) -> Union[Real, None]:
        return self._get('z')

    @property
    def dx(self) -> Union[Real, None]:
        return self._get('dx')

    @property
    def dy(self) -> Union[Real, None]:
        return self._get('dy')

    @property
    def dz(self) -> Union[Real, None]:
        return self._get('dz')

    @property
    def distance(self) -> Union[Range, None]:
        return self._get('distance')

    @property
    def level(self) -> Union[Range, None]:
        return self._get('level')

    @property
    def x_rotation(self) -> Union[Range, None]:
        return self._get('x_rotation')

    @property
    def y_rotation(self) -> Union[Range, None]:
        return self._get('y_rotation')

    @property
    def type(self) -> Union[str, None]:
        return self._get('type')

    @property
    def not_types(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_types')

    @property
    def name(self) -> Union[str, None]:
        return self._get('name')

    @property
    def not_names(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_names')

    @property
    def team(self) -> Union[str, None]:
        return self._get('team')

    @property
    def not_teams(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_teams')

    @property
    def gamemode(self) -> Union[Gamemode, None]:
        return self._get('gamemode')

    @property
    def not_gamemodes(self) -> Union[RepeatableArgument[Gamemode], None]:
        return self._get('not_gamemodes')

    @property
    def tags(self) -> Union[RepeatableArgument[str], None]:
        return self._get('tags')

    @property
    def not_tags(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_tags')

    @property
    def nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self._get('nbts')

    @property
    def not_nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self._get('not_nbts')

    @property
    def scores(self) -> Union[ScoreSet, None]:
        return self._get('scores')

    @property
    def advancements(self) -> Union[AdvancementSet, None]:
        return self._get('advancements')

    @property
    def sort(self) -> Union[SelectorSort, None]:
        return self._get('sort')

    @property
    def limit(self) -> Union[int, None]:
        return self._get('limit')
