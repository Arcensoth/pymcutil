from pymcutil.selector.selector import Selector

BASE = 'r'


class RandomSelector(Selector):
    @classmethod
    def base(cls) -> str:
        return BASE


random = RandomSelector

RANDOM = RandomSelector()
