from pymcutil.command.commands.effect_command import EffectCommand
from pymcutil.command.target import Target

CMD = 'take'


class EffectTakeCommand(EffectCommand):
    """
    An objective model of one of Minecraft's `effect` subcommands:

        effect take <entity> [<effect>]

    http://minecraft.gamepedia.com/Commands#effect
    """

    def __init__(self, target: Target, effect: str = None):
        self.target: Target = target
        self.effect: str = effect

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.target,
            (self.effect, '*'))


take = EffectTakeCommand
