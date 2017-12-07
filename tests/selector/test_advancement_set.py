import unittest

from pymcutil.selector.advancement_set import AdvancementSet


class AdvancementSetTestCase(unittest.TestCase):
    # TODO more tests

    def test(self):
        self.assertEqual(
            '{foo=true,bar=false,custom:something={criterion=true}}',
            str(AdvancementSet(**{'foo': True, 'bar': False, 'custom:something': {'criterion': True}})))
