import unittest

from pymcutil.data_tag.list_data_tag import ListDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class ListDataTagTestCase(unittest.TestCase):
    def test_get(self):
        dt = ListDataTag(['item'])
        self.assertEqual(dt[0], StringDataTag('item'))

    def test_append(self):
        dt = ListDataTag()
        dt.append('item')
        self.assertEqual(dt[0], StringDataTag('item'))

    def test_overwrite(self):
        dt = ListDataTag(['item'])
        dt[0] = 'anotheritem'
        self.assertEqual(dt[0], StringDataTag('anotheritem'))

    def test_del_only(self):
        dt = ListDataTag(['item'])
        self.assertEqual(dt.to_str(), '[item]')
        del dt[0]
        self.assertEqual(dt.to_str(), '[]')

    def test_del_with_remaining(self):
        dt = ListDataTag(['item', 'anotheritem'])
        self.assertEqual(dt.to_str(), '[item,anotheritem]')
        del dt[0]
        self.assertEqual(dt.to_str(), '[anotheritem]')

    def test_default(self):
        dt = ListDataTag()
        self.assertEqual(dt.to_str(), '[]')

    def test_empty_list(self):
        dt = ListDataTag([])
        self.assertEqual(dt.to_str(), '[]')

    def test_multi_empty_lists(self):
        dt = ListDataTag([], [])
        self.assertEqual(dt.to_str(), '[[],[]]')

    def test_multi_nonempty_lists(self):
        dt = ListDataTag(['first'], ['second'])
        self.assertEqual(dt.to_str(), '[[first],[second]]')
