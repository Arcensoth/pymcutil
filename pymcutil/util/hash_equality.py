class HashEquality(object):
    def __eq__(self, other):
        return isinstance(other, self.__class__) and (hash(self) == hash(other))
