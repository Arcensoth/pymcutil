from pymcutil.command.command import Command
from pymcutil.command.target import Target

CMD = 'effect'


class Effect12Command(Command):
    """
    An objective model of Minecraft's `effect` command:

        effect <player> <effect> [seconds] [amplifier] [hideParticles]

    http://minecraft.gamepedia.com/Commands#effect

    *This command is deprecated and will be replaced by `effect <give|take> ...` once 1.13 is released.*
    """

    def __init__(
            self, target: Target, effect: str, seconds: int = None, amplifier: int = None, hide_particles: bool = None):
        self.target: Target = target
        self.effect: str = effect
        self.seconds: int = seconds
        self.amplifier: int = amplifier
        self.hide_particles = hide_particles

    def params(self):
        yield from (
            CMD, self.target, self.effect,
            (self.seconds, 1000000),
            (self.amplifier, 0),
            (self.hide_particles, True))


effect12 = Effect12Command


def effect12_clear(target: Target) -> Effect12Command:
    """ Convenience method for alternate effect command syntax. """
    return effect12(target=target, effect='clear')