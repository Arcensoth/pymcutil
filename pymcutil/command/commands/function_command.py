from pymcutil.command.command import Command
from pymcutil.command.target import Target
from pymcutil.selector import selectors

CMD = 'function'


class FunctionCommand(Command):
    """
    An objective model of Minecraft's `function` command:

        function <function> [if|unless] [selector]

    http://minecraft.gamepedia.com/Commands#function
    """

    def __init__(self, function: str, mode: str = None, mode_target: Target = None):
        self.function: str = function
        self.mode: str = mode
        self.mode_target: Target = mode_target

    def params(self):
        yield from (CMD, self.function, (self.mode, 'if'), (self.mode_target, selectors.SELF))


function = FunctionCommand
