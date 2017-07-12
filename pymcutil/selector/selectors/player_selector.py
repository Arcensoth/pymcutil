from pymcutil.selector.selector import Selector

BASE = 'p'


class PlayerSelector(Selector):
    @property
    def base(self):
        return BASE


player = PlayerSelector

PLAYER = PlayerSelector()
