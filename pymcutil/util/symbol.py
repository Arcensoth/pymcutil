from enum import Enum


class Symbol(Enum):
    def __str__(self):
        return self.value
