import os
import unittest

from pymcutil.util.resources import get_advancement_path, get_function_path, get_loot_table_path, get_resource_name


class ResourcesTestCase(unittest.TestCase):
    def test_get_resource_name(self):
        self.assertEqual(
            get_resource_name(namespace='stuff', components=('foo', 'bar')),
            'stuff:foo/bar')

    def test_get_advancement_path(self):
        self.assertEqual(
            get_advancement_path(root='.', namespace='stuff', components=('foo', 'bar')),
            '{}.{}'.format(os.sep.join(('.', 'data', 'stuff', 'advancements', 'foo', 'bar')), 'json'))

    def test_get_function_path(self):
        self.assertEqual(
            get_function_path(root='.', namespace='stuff', components=('foo', 'bar')),
            '{}.{}'.format(os.sep.join(('.', 'data', 'stuff', 'functions', 'foo', 'bar')), 'mcfunction'))

    def test_get_loot_table_path(self):
        self.assertEqual(
            get_loot_table_path(root='.', namespace='stuff', components=('foo', 'bar')),
            '{}.{}'.format(os.sep.join(('.', 'data', 'stuff', 'loot_tables', 'foo', 'bar')), 'json'))
