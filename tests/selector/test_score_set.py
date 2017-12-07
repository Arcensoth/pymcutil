import unittest

from pymcutil.selector.score_set import ScoreSet


class ScoreSetTestCase(unittest.TestCase):
    # TODO more tests

    def test(self):
        self.assertEqual(
            '{foo=1,bar=1..5}',
            str(ScoreSet(foo=1, bar=(1, 5))))
