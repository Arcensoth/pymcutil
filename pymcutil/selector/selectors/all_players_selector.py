from pymcutil.selector.selector import Selector

BASE = 'a'


class AllPlayersSelector(Selector):
    @property
    def base(self) -> str:
        return BASE


all_players = AllPlayersSelector

ALL_PLAYERS = AllPlayersSelector()
