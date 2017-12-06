from typing import Iterable

from pymcutil.command import commands
from pymcutil.command.command import Command
from pymcutil.resource.resource_generator.abc.procedure import Procedure
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from . import functions


def split_in_two(s):
    index = len(s) // 2
    s1, s2 = s[:index], s[index:]
    return s1, s2


class StringSplitProcedure(Procedure):
    def commands(
            self, manager: ResourceManager, reference: functions.StringSplitFunctionResourceReference) -> Iterable[Command]:
        message, indent = reference.params
        yield commands.say(message='. . ' * indent + message)
        if len(message) > 1:
            former, latter = split_in_two(message)
            yield commands.function(function=manager.name(functions.string_split(former, indent + 1)))
            yield commands.function(function=manager.name(functions.string_split(latter, indent + 1)))


string_split = StringSplitProcedure
