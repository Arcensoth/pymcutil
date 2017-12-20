from pymcutil.selector.abc.selector import Selector
from pymcutil.symbols import selector_bases
from pymcutil.symbols.selector_bases.selector_bases import SelectorBase


class AllPlayersSelector(Selector):
    @property
    def base(self) -> SelectorBase:
        return selector_bases.all_players


all_players = AllPlayersSelector

ALL_PLAYERS = AllPlayersSelector()
