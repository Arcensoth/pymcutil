from numbers import Real
from typing import Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.repeatable_argument import RepeatableArgument
from pymcutil.selector.score_set import ScoreSet
from pymcutil.symbols.gamemodes.gamemode import Gamemode
from pymcutil.symbols.selector_sorts.selector_sort import SelectorSort
from pymcutil.util.data_map import DataMap


class SelectorArguments(DataMap):
    def __init__(
            self,
            x: Real = None, y: Real = None, z: Real = None,
            dx: Real = None, dy: Real = None, dz: Real = None,
            x_rotation: Range = None, y_rotation: Range = None,
            distance: Range = None,
            level: Range = None,
            type: str = None, not_types: RepeatableArgument[str] = None,
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
            level=level, type=type, not_types=not_types, name=name, not_names=not_names, team=team,
            not_teams=not_teams, gamemode=gamemode, not_gamemodes=not_gamemodes, tags=tags, not_tags=not_tags,
            nbts=nbts, not_nbts=not_nbts, scores=scores, advancements=advancements, sort=sort, limit=limit,
        )

    def __str__(self):
        return ''.join(('[', ','.join(['{}={}'.format(k, v) for k, v in self.items()]), ']'))

    @property
    def x(self) -> Union[Real, None]:
        return self._get('x')

    @x.setter
    def x(self, value: Real):
        self._set('x', value, Real)

    @x.deleter
    def x(self):
        self._del('x')

    @property
    def y(self) -> Union[Real, None]:
        return self._get('y')

    @y.setter
    def y(self, value: Real):
        self._set('y', value, Real)

    @y.deleter
    def y(self):
        self._del('y')

    @property
    def z(self) -> Union[Real, None]:
        return self._get('z')

    @z.setter
    def z(self, value: Real):
        self._set('z', value, Real)

    @z.deleter
    def z(self):
        self._del('z')

    @property
    def dx(self) -> Union[Real, None]:
        return self._get('dx')

    @dx.setter
    def dx(self, value: Real):
        self._set('dx', value, Real)

    @dx.deleter
    def dx(self):
        self._del('dx')

    @property
    def dy(self) -> Union[Real, None]:
        return self._get('dy')

    @dy.setter
    def dy(self, value: Real):
        self._set('dy', value, Real)

    @dy.deleter
    def dy(self):
        self._del('dy')

    @property
    def dz(self) -> Union[Real, None]:
        return self._get('dz')

    @dz.setter
    def dz(self, value: Real):
        self._set('dz', value, Real)

    @dz.deleter
    def dz(self):
        self._del('dz')

    @property
    def distance(self) -> Union[Range, None]:
        return self._get('distance')

    @distance.setter
    def distance(self, value: Range):
        self._set('distance', value, Range)

    @distance.deleter
    def distance(self):
        self._del('distance')

    @property
    def level(self) -> Union[Range, None]:
        return self._get('level')

    @level.setter
    def level(self, value: Range):
        self._set('level', value, Range)

    @level.deleter
    def level(self):
        self._del('level')

    @property
    def x_rotation(self) -> Union[Range, None]:
        return self._get('x_rotation')

    @x_rotation.setter
    def x_rotation(self, value: Range):
        self._set('x_rotation', value, Range)

    @x_rotation.deleter
    def x_rotation(self):
        self._del('x_rotation')

    @property
    def y_rotation(self) -> Union[Range, None]:
        return self._get('y_rotation')

    @y_rotation.setter
    def y_rotation(self, value: Range):
        self._set('y_rotation', value, Range)

    @y_rotation.deleter
    def y_rotation(self):
        self._del('y_rotation')

    @property
    def type(self) -> Union[str, None]:
        return self._get('type')

    @type.setter
    def type(self, value: str):
        self._set('type', value, str)

    @type.deleter
    def type(self):
        self._del('type')

    @property
    def not_types(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_types')

    @not_types.setter
    def not_types(self, value: RepeatableArgument[str]):
        self._set('not_types', value, RepeatableArgument)

    @not_types.deleter
    def not_types(self):
        self._del('not_types')

    @property
    def name(self) -> Union[str, None]:
        return self._get('name')

    @name.setter
    def name(self, value: str):
        self._set('name', value, str)

    @name.deleter
    def name(self):
        self._del('name')

    @property
    def not_names(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_names')

    @not_names.setter
    def not_names(self, value: RepeatableArgument[str]):
        self._set('not_names', value, RepeatableArgument)

    @not_names.deleter
    def not_names(self):
        self._del('not_names')

    @property
    def team(self) -> Union[str, None]:
        return self._get('team')

    @team.setter
    def team(self, value: str):
        self._set('team', value, str)

    @team.deleter
    def team(self):
        self._del('team')

    @property
    def not_teams(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_teams')

    @not_teams.setter
    def not_teams(self, value: RepeatableArgument[str]):
        self._set('not_teams', value, RepeatableArgument)

    @not_teams.deleter
    def not_teams(self):
        self._del('not_teams')

    @property
    def gamemode(self) -> Union[Gamemode, None]:
        return self._get('gamemode')

    @gamemode.setter
    def gamemode(self, value: Gamemode):
        self._set('gamemode', value, Gamemode)

    @gamemode.deleter
    def gamemode(self):
        self._del('gamemode')

    @property
    def not_gamemodes(self) -> Union[RepeatableArgument[Gamemode], None]:
        return self._get('not_gamemodes')

    @not_gamemodes.setter
    def not_gamemodes(self, value: RepeatableArgument[Gamemode]):
        self._set('not_gamemodes', value, RepeatableArgument)

    @not_gamemodes.deleter
    def not_gamemodes(self):
        self._del('not_gamemodes')

    @property
    def tags(self) -> Union[RepeatableArgument[str], None]:
        return self._get('tags')

    @tags.setter
    def tags(self, value: RepeatableArgument[str]):
        self._set('tags', value, RepeatableArgument)

    @tags.deleter
    def tags(self):
        self._del('tags')

    @property
    def not_tags(self) -> Union[RepeatableArgument[str], None]:
        return self._get('not_tags')

    @not_tags.setter
    def not_tags(self, value: RepeatableArgument[str]):
        self._set('not_tags', value, RepeatableArgument)

    @not_tags.deleter
    def not_tags(self):
        self._del('not_tags')

    @property
    def nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self._get('nbts')

    @nbts.setter
    def nbts(self, value: RepeatableArgument[CompoundDataTag]):
        self._set('nbts', value, RepeatableArgument)

    @nbts.deleter
    def nbts(self):
        self._del('nbts')

    @property
    def not_nbts(self) -> Union[RepeatableArgument[CompoundDataTag], None]:
        return self._get('not_nbts')

    @not_nbts.setter
    def not_nbts(self, value: RepeatableArgument[CompoundDataTag]):
        self._set('not_nbts', value, RepeatableArgument)

    @not_nbts.deleter
    def not_nbts(self):
        self._del('not_nbts')

    @property
    def scores(self) -> Union[ScoreSet, None]:
        return self._get('scores')

    @scores.setter
    def scores(self, value: ScoreSet):
        self._set('scores', value, ScoreSet)

    @scores.deleter
    def scores(self):
        self._del('scores')

    @property
    def advancements(self) -> Union[AdvancementSet, None]:
        return self._get('advancements')

    @advancements.setter
    def advancements(self, value: AdvancementSet):
        self._set('advancements', value, AdvancementSet)

    @advancements.deleter
    def advancements(self):
        self._del('advancements')

    @property
    def sort(self) -> Union[SelectorSort, None]:
        return self._get('sort')

    @sort.setter
    def sort(self, value: SelectorSort):
        self._set('sort', value, SelectorSort)

    @sort.deleter
    def sort(self):
        self._del('sort')

    @property
    def limit(self) -> Union[int, None]:
        return self._get('limit')

    @limit.setter
    def limit(self, value: int):
        self._set('limit', value, int)

    @limit.deleter
    def limit(self):
        self._del('limit')
