import logging
import tempfile
import unittest
from typing import Iterable

from pymcutil.command import commands
from pymcutil.command.command import Command
from pymcutil.resource.resource_generator.abc.procedure import Procedure
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_manager.stacked_resource_manager import StackedResourceManager
from pymcutil.resource.resource_reference.function_reference import FunctionReference

log = logging.getLogger(__name__)


class HelloFunctionReference(FunctionReference):
    # If another function references the 'hello' function, it will need to specify <count> and <subject>.
    def __init__(self, subject: str, count: int):
        super().__init__(subject, count)


class HelloProcedure(Procedure):
    def keys(self, subject: str, count: int) -> Iterable:
        yield from (subject, str(count))

    def run(self, subject: str, count: int) -> Iterable[Command]:
        # Say hello <count> times.
        yield from ([commands.say(message='Hello {}!'.format(subject))] * count)

        # Call the same function with one less <count>, so long as we can keep counting down.
        if count > 1:
            yield commands.function(HelloFunctionReference(subject, count - 1))


class HelloE2ETestCase(unittest.TestCase):
    def test(self):
        mapping = {
            HelloFunctionReference: HelloProcedure(namespace='pymcutil', root='hello')
        }

        tempdir = tempfile.TemporaryDirectory()

        rm: ResourceManager = StackedResourceManager(
            mapping=mapping, output_root=tempdir.name)

        resources = list(rm.generate(
            HelloFunctionReference('world', 3)))

        print('\n'.join(str(r) for r in resources))

        tempdir.cleanup()
