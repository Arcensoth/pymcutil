import unittest

from pymcutil.block.block_state import BlockState


class BlockStateTestCase(unittest.TestCase):
    def test_eq(self):
        bs = BlockState(color='blue')
        self.assertEqual(bs, BlockState(color='blue'))

    def test_getitem(self):
        bs = BlockState(half='bottom', variant='quartz')
        self.assertEqual(bs['half'], 'bottom')
        self.assertEqual(bs['variant'], 'quartz')

    def test_len_0(self):
        bs0 = BlockState()
        self.assertEqual(len(bs0), 0)

    def test_len_1(self):
        bs1 = BlockState(color='blue')
        self.assertEqual(len(bs1), 1)

    def test_len_2(self):
        bs2 = BlockState(half='bottom', variant='quartz')
        self.assertEqual(len(bs2), 2)

    def test_delitem(self):
        bs = BlockState(half='bottom', variant='quartz')
        self.assertEqual(bs['variant'], 'quartz')
        del bs['variant']
        with self.assertRaises(KeyError):
            shouldfail = bs['variant']

    def test_setitem(self):
        bs = BlockState()
        bs['color'] = 'blue'
        self.assertEqual(bs['color'], 'blue')

    def test_setitem_bad_key_str(self):
        bs = BlockState()
        with self.assertRaises(KeyError):
            bs['bad key'] = 'goodvalue'

    def test_setitem_bad_key_obj(self):
        bs = BlockState()
        with self.assertRaises(KeyError):
            bs[{'bad', 'obj'}] = 'goodvalue'

    def test_setitem_bad_value_str(self):
        bs = BlockState()
        with self.assertRaises(ValueError):
            bs['goodkey'] = 'bad value'

    def test_setitem_bad_value_obj(self):
        bs = BlockState()
        with self.assertRaises(ValueError):
            bs['goodkey'] = {'bad', 'obj'}

    def test_set_then_get(self):
        bs = BlockState()
        bs['color'] = 'blue'
        self.assertEqual(bs['color'], 'blue')

    def test_overwrite(self):
        bs = BlockState(color='blue')
        self.assertEqual(bs['color'], 'blue')
        bs['color'] = 'red'
        self.assertEqual(bs['color'], 'red')

    def test_bool_false(self):
        bs = BlockState(powered=False)
        self.assertEqual(bs['powered'], False)

    def test_bool_true(self):
        bs = BlockState(powered=True)
        self.assertEqual(bs['powered'], True)

    def test_int_value(self):
        bs = BlockState(age=4)
        self.assertEqual(bs['age'], 4)

    def test_str_default(self):
        bs = BlockState()
        self.assertEqual(str(bs), 'default')

    def test_str_with_str_values(self):
        bs = BlockState(half='bottom', variant='quartz')
        self.assertEqual(
            set(str(bs).split(',')),
            set('half=bottom,variant=quartz'.split(',')))

    def test_str_with_all_values(self):
        bs = BlockState(powered=True, age=7, color='green')
        self.assertEqual(
            set(str(bs).split(',')),
            set('powered=true,age=7,color=green'.split(',')))
