from pymcutil.selector.selector import Selector

BASE = 'p'


class PlayerSelector(Selector):
    @classmethod
    def base(cls):
        return BASE


player = PlayerSelector

PLAYER = PlayerSelector()
