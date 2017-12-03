import logging
import tempfile
import unittest

from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_database.forgetful_resource_database import ForgetfulResourceDatabase
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_manager.standard_resource_manager import StandardResourceManager
from . import functions, procedures

log = logging.getLogger(__name__)


class StringSplitE2ETestCase(unittest.TestCase):
    def test(self):
        tempdir = tempfile.TemporaryDirectory()
        log.info('Using temporary directory: {}'.format(tempdir.name))

        database: ResourceDatabase = ForgetfulResourceDatabase(tempdir.name)

        registry = (
            (functions.string_split, procedures.string_split(namespace='string_split')),
        )

        manager: ResourceManager = StandardResourceManager(database, registry)

        root_lrs = list(manager.generate(reference) for reference in (
            functions.string_split(message='abcdefghi', indent=0),
            functions.string_split(message='xyz', indent=0),
        ))

        log.info('Generated {} root resources:'.format(len(root_lrs)))
        for root_lr in root_lrs:
            log.info('    {} ({})'.format(root_lr.location.name, root_lr.location.path))

        all_lrs = list(database.all())
        log.info('Generated {} resources overall:'.format(len(all_lrs)))
        for lr in all_lrs:
            log.info('    {} ({})'.format(lr.location.name, lr.location.path))
            for line in lr.resource.text.split('\n'):
                log.debug('        {}'.format(line))

        tempdir.cleanup()
