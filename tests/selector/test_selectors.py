import unittest

from pymcutil.position.position import Position
from pymcutil.selector import selectors


class SelectorTestCase(unittest.TestCase):
    def test_base_player(self):
        self.assertEqual(
            str(selectors.PLAYER),
            '@p')

    def test_base_random(self):
        self.assertEqual(
            str(selectors.RANDOM),
            '@r')

    def test_base_all_players(self):
        self.assertEqual(
            str(selectors.ALL_PLAYERS),
            '@a')

    def test_base_entities(self):
        self.assertEqual(
            str(selectors.ENTITIES),
            '@e')

    def test_base_self(self):
        self.assertEqual(
            str(selectors.SELF),
            '@s')

    def test_argument_position(self):
        self.assertEqual(
            str(selectors.entities(position=Position(1, 2, 3))),
            '@e[x=1,y=2,z=3]')

    def test_argument_volume(self):
        self.assertEqual(
            str(selectors.entities(volume=Position(4, 9, 16))),
            '@e[dx=4,dy=9,dz=16]')

    def test_argument_entity_type(self):
        self.assertEqual(
            str(selectors.entities(entity_type='area_effect_cloud')),
            '@e[type=area_effect_cloud]')

    def test_argument_l(self):
        self.assertEqual(
            str(selectors.entities(l=10)),
            '@e[l=10]')

    def test_argument_lm(self):
        self.assertEqual(
            str(selectors.entities(lm=5)),
            '@e[lm=5]')

    def test_argument_m(self):
        self.assertEqual(
            str(selectors.entities(m=3)),
            '@e[m=3]')

    def test_argument_team(self):
        self.assertEqual(
            str(selectors.entities(team='myteam')),
            '@e[team=myteam]')

    def test_argument_max_scores(self):
        self.assertEqual(
            str(selectors.entities(max_scores=dict(myobjective=100))),
            '@e[score_myobjective=100]')

    def test_argument_min_scores(self):
        self.assertEqual(
            str(selectors.entities(min_scores=dict(myobjective=1))),
            '@e[score_myobjective_min=1]')

    def test_argument_exact_score(self):
        self.assertEqual(
            str(selectors.entities(exact_scores=dict(myobjective=50))),
            '@e[score_myobjective=50,score_myobjective_min=50]')

    def test_argument_name(self):
        self.assertEqual(
            str(selectors.entities(name='myname')),
            '@e[name=myname]')

    def test_argument_tag(self):
        self.assertEqual(
            str(selectors.entities(tag='mytag')),
            '@e[tag=mytag]')

    def test_argument_r(self):
        self.assertEqual(
            str(selectors.entities(r=90)),
            '@e[r=90]')

    def test_argument_rm(self):
        self.assertEqual(
            str(selectors.entities(rm=45)),
            '@e[rm=45]')

    def test_argument_rx(self):
        self.assertEqual(
            str(selectors.entities(rx=31.4159)),
            '@e[rx=31.4]')

    def test_argument_rxm(self):
        self.assertEqual(
            str(selectors.entities(rxm=27.1828)),
            '@e[rxm=27.2]')

    def test_argument_ry(self):
        self.assertEqual(
            str(selectors.entities(ry=31.4159)),
            '@e[ry=31.4]')

    def test_argument_rym(self):
        self.assertEqual(
            str(selectors.entities(rym=27.1828)),
            '@e[rym=27.2]')

    def test_argument_c(self):
        self.assertEqual(
            str(selectors.entities(c=1)),
            '@e[c=1]')

    def test_everything(self):
        self.assertEqual(
            str(selectors.entities(
                position=Position(1, 2, 3),
                volume=Position(4, 9, 16),
                entity_type='area_effect_cloud',
                l=10,
                lm=5,
                m=3,
                team='myteam',
                max_scores={'myobjective': 100},
                min_scores={'myobjective': 1},
                name='myname',
                tag='mytag',
                r=90,
                rm=45,
                rx=31.4159,
                rxm=27.1828,
                ry=31.4159,
                rym=27.1828,
                c=1
            )),
            '@e[x=1,y=2,z=3,dx=4,dy=9,dz=16,type=area_effect_cloud,l=10,lm=5,m=3,team=myteam,score_myobjective=100,'
            'score_myobjective_min=1,name=myname,tag=mytag,r=90,rm=45,rx=31.4,rxm=27.2,ry=31.4,rym=27.2,c=1]')
