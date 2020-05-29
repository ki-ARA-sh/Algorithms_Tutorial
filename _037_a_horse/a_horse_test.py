from unittest import TestCase
from _037_a_horse.a_horse import horse_moves


class HorseMovesTest(TestCase):

    def test1(self):
        n = 3
        self.assertEqual(3, len(horse_moves((0, 0), 3, 2, [0, 1, 2])))

    def test2(self):
        n = 3
        self.assertEqual(4, len(horse_moves((0, 0), 3, 4, [0, 1, 2])))
