from typing import Iterable

from pymcutil.command import commands
from pymcutil.command.command import Command
from pymcutil.resource.resource_generator.abc.procedure import Procedure
from pymcutil.resource.resource_manager.standard_resource_manager import ResourceManager
from tests.e2e.string_split import functions
from tests.e2e.string_split.functions import StringSplitFunctionReference


def split_in_two(s):
    index = len(s) // 2
    s1, s2 = s[:index], s[index:]
    return s1, s2


class StringSplitProcedure(Procedure):
    def commands(self, manager: ResourceManager, reference: StringSplitFunctionReference) -> Iterable[Command]:
        letters, = reference.params
        yield commands.say(message=letters)
        if len(letters) > 1:
            former, latter = split_in_two(letters)
            yield commands.function(function=manager.refer(functions.string_split(former)))
            yield commands.function(function=manager.refer(functions.string_split(latter)))


string_split = StringSplitProcedure
