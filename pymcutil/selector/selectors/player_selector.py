from typing import Dict

from pymcutil.position.position import Position
from pymcutil.selector.selector import Selector

BASE = 'p'


class PlayerSelector(Selector):
    @property
    def base(self):
        return BASE


def player(
        position: Position = None, volume: Position = None, entity_type: str = None,
        l: int = None, lm: int = None, m: int = None, team: str = None,
        min_scores: Dict[str, int] = None, max_scores: Dict[str, int] = None,
        name: str = None, tag: str = None, r: int = None, rm: int = None,
        rx: float = None, rxm: float = None, ry: float = None, rym: float = None,
        c: int = None, exact_scores: Dict[str, int] = None) -> PlayerSelector:
    """ Functional alias for creating `PlayerSelector` instances. """
    return PlayerSelector(**locals())


PLAYER = PlayerSelector()
