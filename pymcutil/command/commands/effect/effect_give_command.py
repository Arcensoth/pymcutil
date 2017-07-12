from pymcutil.command.commands.effect_command import EffectCommand
from pymcutil.command.target import Target

CMD = 'give'


class EffectGiveCommand(EffectCommand):
    """
    An objective model of one of Minecraft's `effect` subcommands:

        effect give <entity> <effect> [seconds] [amplifier] [hideParticles]

    http://minecraft.gamepedia.com/Commands#effect
    """

    def __init__(
            self, target: Target, effect: str, seconds: int = None, amplifier: int = None, hide_particles: bool = None):
        self.target: Target = target
        self.effect: str = effect
        self.seconds: int = seconds
        self.amplifier: int = amplifier
        self.hide_particles = hide_particles

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.target, self.effect,
            (self.seconds, 1000000),
            (self.amplifier, 0),
            (self.hide_particles, True))


give = EffectGiveCommand
