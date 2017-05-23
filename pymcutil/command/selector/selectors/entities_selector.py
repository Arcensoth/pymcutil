from typing import Dict

from pymcutil.command.selector.selector import Selector
from pymcutil.position.position import Position

BASE = 'e'


class EntitiesSelector(Selector):
    @property
    def base(self):
        return BASE


def entities(
        position: Position = None, volume: Position = None, entity_type: str = None,
        l: int = None, lm: int = None, m: int = None, team: str = None,
        min_scores: Dict[str, int] = None, max_scores: Dict[str, int] = None,
        name: str = None, tag: str = None, r: int = None, rm: int = None,
        rx: float = None, rxm: float = None, ry: float = None, rym: float = None,
        c: int = None, exact_scores: Dict[str, int] = None) -> EntitiesSelector:
    """ Functional alias for creating `EntitiesSelector` instances. """
    return EntitiesSelector(**locals())
