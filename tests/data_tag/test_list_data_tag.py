import unittest

from pymcutil.data_tag.list_data_tag import ListDataTag
from pymcutil.data_tag.string_data_tag import StringDataTag


class ListDataTagTestCase(unittest.TestCase):
    def test_get(self):
        dt = ListDataTag(['item'])
        self.assertEqual(dt[0], StringDataTag('item'))
        self.assertEqual(dt.to_str(), '[item]')

    def test_append(self):
        dt = ListDataTag()
        dt.append('item')
        self.assertEqual(dt[0], StringDataTag('item'))
        self.assertEqual(dt.to_str(), '[item]')

    def test_insert(self):
        dt = ListDataTag(['item', 'anotheritem'])
        dt.insert(1, 'middleitem')
        self.assertEqual(dt[1], StringDataTag('middleitem'))
        self.assertEqual(dt.to_str(), '[item,middleitem,anotheritem]')

    def test_overwrite(self):
        dt = ListDataTag(['item'])
        dt[0] = 'anotheritem'
        self.assertEqual(dt[0], StringDataTag('anotheritem'))
        self.assertEqual(dt.to_str(), '[anotheritem]')

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

    def test_breaking_string(self):
        dt = ListDataTag(['my:string'])
        self.assertEqual(dt.to_str(), '["my:string"]')

    def test_quoted_string(self):
        dt = ListDataTag(['my"string'])
        self.assertEqual(dt.to_str(), r'["my\"string"]')

    def test_init_with_many_values(self):
        dt = ListDataTag([True, 123456789, 123.5, 'mystring', [], {}])
        self.assertEqual(dt.to_str(), '[1b,123456789,123.5d,mystring,[],{}]')

    def test_append_with_many_values(self):
        dt = ListDataTag()
        dt.append(True)
        dt.append(123456789)
        dt.append(123.5)
        dt.append('mystring')
        dt.append([])
        dt.append({})
        self.assertEqual(dt.to_str(), '[1b,123456789,123.5d,mystring,[],{}]')

    def test_addition_with_many_values(self):
        dt = ListDataTag()
        dt += [True, 123456789, 123.5, 'mystring', [], {}]
        self.assertEqual(dt.to_str(), '[1b,123456789,123.5d,mystring,[],{}]')

    def test_deep_conversion(self):
        dt = ListDataTag([[[[[True, 123456789, 123.5, 'mystring', [], {}]]]]])
        self.assertEqual(dt.to_str(), '[[[[[1b,123456789,123.5d,mystring,[],{}]]]]]')
