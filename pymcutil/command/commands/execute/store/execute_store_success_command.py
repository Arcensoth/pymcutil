from .._execute_store_command import ExecuteStoreCommand

CMD = 'success'


class ExecuteStoreSuccessCommand(ExecuteStoreCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute store success <name: entity> <objective: string> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.target, self.objective,
            (self.subcommand.substr(), None))


success = ExecuteStoreSuccessCommand
