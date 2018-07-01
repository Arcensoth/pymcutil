from pymcutil.util.symbol import Symbol


class SelectorBase(Symbol):
    pass


all_players = SelectorBase('a')
entities = SelectorBase('e')
player = SelectorBase('p')
random = SelectorBase('r')
self = SelectorBase('s')
