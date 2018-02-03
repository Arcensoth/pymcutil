import unittest

from pymcutil.selector import selectors


class SelectorTestCase(unittest.TestCase):
    def test_base_player(self):
        self.assertEqual(
            '@p',
            str(selectors.PLAYER))

    def test_base_random(self):
        self.assertEqual(
            '@r',
            str(selectors.RANDOM))

    def test_base_all_players(self):
        self.assertEqual(
            '@a',
            str(selectors.ALL_PLAYERS))

    def test_base_entities(self):
        self.assertEqual(
            '@e',
            str(selectors.ENTITIES))

    def test_base_self(self):
        self.assertEqual(
            '@s',
            str(selectors.SELF))

    def test_argument_position(self):
        self.assertEqual(
            '@e[x=1.0,y=2.0,z=3.0]',
            str(selectors.entities(position=(1, 2, 3))))

    def test_argument_position_with_floats(self):
        self.assertEqual(
            '@e[x=1.9,y=2.5,z=3.1]',
            str(selectors.entities(position=(1.9, 2.5, 3.1))))

    def test_argument_volume(self):
        self.assertEqual(
            '@e[dx=4.0,dy=9.0,dz=16.0]',
            str(selectors.entities(volume=(4, 9, 16))))

    def test_argument_volume_with_floats(self):
        self.assertEqual(
            '@e[dx=4.9,dy=9.5,dz=16.1]',
            str(selectors.entities(volume=(4.9, 9.5, 16.1))))

    def test_argument_tags(self):
        self.assertEqual(
            '@e[tag=foo,tag=bar]',
            str(selectors.entities(tags=['foo', 'bar'])))

    def test_argument_not_tags(self):
        self.assertEqual(
            '@e[tag=!foo,tag=!bar]',
            str(selectors.entities(not_tags=['foo', 'bar'])))

    # def test_argument_type(self):
    #     self.assertEqual(
    #         '@e[type=area_effect_cloud]',
    #         str(selectors.entities(type='area_effect_cloud')))
    #
    # def test_argument_not_types(self):
    #     self.assertEqual(
    #         '@e[type=!area_effect_cloud]',
    #         str(selectors.entities(not_types=['area_effect_cloud'])))
    #
    # def test_argument_not_entity_types(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_type=('cow', 'pig'))),
    #         '@e[type=!cow,type=!pig]')
    #
    # def test_argument_l(self):
    #     self.assertEqual(
    #         str(selectors.entities(l=10)),
    #         '@e[l=10]')
    #
    # def test_argument_lm(self):
    #     self.assertEqual(
    #         str(selectors.entities(lm=5)),
    #         '@e[lm=5]')
    #
    # def test_argument_m(self):
    #     self.assertEqual(
    #         str(selectors.entities(m='survival')),
    #         '@e[m=survival]')
    #
    # def test_argument_not_m(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_m='survival')),
    #         '@e[m=!survival]')
    #
    # def test_argument_not_ms(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_m=('survival', 'adventure'))),
    #         '@e[m=!survival,m=!adventure]')
    #
    # def test_argument_team(self):
    #     self.assertEqual(
    #         str(selectors.entities(team='myteam')),
    #         '@e[team=myteam]')
    #
    # def test_argument_not_team(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_team='myteam')),
    #         '@e[team=!myteam]')
    #
    # def test_argument_not_teams(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_team=('myteam', 'otherteam'))),
    #         '@e[team=!myteam,team=!otherteam]')
    #
    # def test_argument_max_scores(self):
    #     self.assertEqual(
    #         str(selectors.entities(max_scores={'myobjective': 100})),
    #         '@e[score_myobjective=100]')
    #
    # def test_argument_min_scores(self):
    #     self.assertEqual(
    #         str(selectors.entities(min_scores={'myobjective': 1})),
    #         '@e[score_myobjective_min=1]')
    #
    # def test_argument_exact_score(self):
    #     self.assertEqual(
    #         str(selectors.entities(exact_scores={'myobjective': 50})),
    #         '@e[score_myobjective=50,score_myobjective_min=50]')
    #
    # def test_argument_name(self):
    #     self.assertEqual(
    #         str(selectors.entities(name='myname')),
    #         '@e[name=myname]')
    #
    # def test_argument_not_name(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_name='myname')),
    #         '@e[name=!myname]')
    #
    # def test_argument_not_names(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_name=('myname', 'othername'))),
    #         '@e[name=!myname,name=!othername]')
    #
    # def test_argument_tag(self):
    #     self.assertEqual(
    #         str(selectors.entities(tag='mytag')),
    #         '@e[tag=mytag]')
    #
    # def test_argument_tags(self):
    #     self.assertEqual(
    #         str(selectors.entities(tag=('mytag', 'othertag'))),
    #         '@e[tag=mytag,tag=othertag]')
    #
    # def test_argument_not_tag(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_tag='mytag')),
    #         '@e[tag=!mytag]')
    #
    # def test_argument_not_tags(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_tag=('mytag', 'othertag'))),
    #         '@e[tag=!mytag,tag=!othertag]')
    #
    # def test_argument_r(self):
    #     self.assertEqual(
    #         str(selectors.entities(r=90)),
    #         '@e[r=90.0]')
    #
    # def test_argument_rm(self):
    #     self.assertEqual(
    #         str(selectors.entities(rm=45)),
    #         '@e[rm=45.0]')
    #
    # def test_argument_rx(self):
    #     self.assertEqual(
    #         str(selectors.entities(rx=31.4159)),
    #         '@e[rx=31.4]')
    #
    # def test_argument_rxm(self):
    #     self.assertEqual(
    #         str(selectors.entities(rxm=27.1828)),
    #         '@e[rxm=27.2]')
    #
    # def test_argument_ry(self):
    #     self.assertEqual(
    #         str(selectors.entities(ry=31.4159)),
    #         '@e[ry=31.4]')
    #
    # def test_argument_rym(self):
    #     self.assertEqual(
    #         str(selectors.entities(rym=27.1828)),
    #         '@e[rym=27.2]')
    #
    # def test_argument_nbt(self):
    #     self.assertEqual(
    #         str(selectors.entities(nbt={'CustomName': 'Spacey Spacington'})),
    #         '@e[nbt={CustomName:"Spacey Spacington"}]')
    #
    # def test_argument_nbts(self):
    #     self.assertEqual(
    #         str(selectors.entities(nbt=({'CustomName': 'Spacey Spacington'}, {'NoAI': True}))),
    #         '@e[nbt={CustomName:"Spacey Spacington"},nbt={NoAI:1b}]')
    #
    # def test_argument_not_nbt(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_nbt={'CustomName': 'Spacey Spacington'})),
    #         '@e[nbt=!{CustomName:"Spacey Spacington"}]')
    #
    # def test_argument_not_nbts(self):
    #     self.assertEqual(
    #         str(selectors.entities(not_nbt=({'CustomName': 'Spacey Spacington'}, {'NoAI': True}))),
    #         '@e[nbt=!{CustomName:"Spacey Spacington"},nbt=!{NoAI:1b}]')
    #
    # def test_argument_c(self):
    #     self.assertEqual(
    #         str(selectors.entities(c=1)),
    #         '@e[c=1]')
    #
    # def test_everything(self):
    #     self.assertEqual(
    #         str(selectors.entities(
    #             position=Position(1.5, 2, 3.5),
    #             volume=Position(4, 9.5, 16),
    #             type='area_effect_cloud',
    #             l=10,
    #             lm=5,
    #             m='survival',
    #             team='myteam',
    #             max_scores={'myobjective': 100},
    #             min_scores={'myobjective': 1},
    #             name='myname',
    #             tag='mytag',
    #             r=90,
    #             rm=45,
    #             rx=31.4159,
    #             rxm=27.1828,
    #             ry=31.4159,
    #             rym=27.1828,
    #             nbt={'CustomName': 'Spacey Spacington'},
    #             c=1
    #         )),
    #         '@e[x=1.5,y=2.0,z=3.5,dx=4.0,dy=9.5,dz=16.0,type=area_effect_cloud,l=10,lm=5,m=survival,team=myteam,'
    #         'score_myobjective=100,score_myobjective_min=1,name=myname,tag=mytag,'
    #         'r=90.0,rm=45.0,rx=31.4,rxm=27.2,ry=31.4,rym=27.2,nbt={CustomName:"Spacey Spacington"},c=1]')
