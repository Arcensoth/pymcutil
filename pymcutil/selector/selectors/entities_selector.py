from pymcutil.selector.selector import Selector

BASE = 'e'


class EntitiesSelector(Selector):
    @classmethod
    def base(cls):
        return BASE


entities = EntitiesSelector

ENTITIES = EntitiesSelector()
