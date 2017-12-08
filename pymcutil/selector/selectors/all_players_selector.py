from pymcutil.selector.selector import Selector

BASE = 'a'


class AllPlayersSelector(Selector):
    @classmethod
    def base(cls):
        return BASE


all_players = AllPlayersSelector

ALL_PLAYERS = AllPlayersSelector()
