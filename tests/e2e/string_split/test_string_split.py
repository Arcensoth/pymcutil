import tempfile
import unittest

from pymcutil.resource.resource_database.forgetful_resource_database import ForgetfulResourceDatabase
from pymcutil.resource.resource_manager.standard_resource_manager import StandardResourceManager, ResourceManager
from tests.e2e.string_split import functions, procedures


class StringSplitE2ETestCase(unittest.TestCase):
    def test(self):
        tempdir = tempfile.TemporaryDirectory()

        database = ForgetfulResourceDatabase(tempdir.name)

        registry = (
            (functions.string_split, procedures.string_split(namespace='string_split')),
        )

        manager: ResourceManager = StandardResourceManager(database, registry)

        resources = list(manager.generate(
            functions.string_split('ABCDEFGH'),
            functions.string_split('XYZ')))

        print('\n'.join(str(r) for r in resources))  # TEMP

        tempdir.cleanup()
