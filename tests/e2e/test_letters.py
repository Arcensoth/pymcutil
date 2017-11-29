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


def split_in_two(s):
    index = len(s) // 2
    s1, s2 = s[:index], s[index:]
    return s1, s2


class LettersFunctionReference(FunctionReference):
    def __init__(self, letters: str):
        super().__init__(letters)


class LettersProcedure(Procedure):
    def keys(self, letters: str) -> Iterable:
        yield letters

    def run(self, letters: str) -> Iterable[Command]:
        yield commands.say(message=letters)
        if len(letters) > 1:
            former, latter = split_in_two(letters)
            yield commands.function(LettersFunctionReference(former))
            yield commands.function(LettersFunctionReference(latter))


class LettersE2ETestCase(unittest.TestCase):
    def test(self):
        mapping = {
            LettersFunctionReference: LettersProcedure(namespace='pymcutil', root='letters')
        }

        tempdir = tempfile.TemporaryDirectory()

        rm: ResourceManager = StackedResourceManager(
            mapping=mapping, output_root=tempdir.name)

        resources = list(rm.generate(
            LettersFunctionReference('ABCDEFGH')))

        print('\n'.join(str(r) for r in resources))

        tempdir.cleanup()
