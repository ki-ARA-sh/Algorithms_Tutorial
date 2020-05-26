from unittest import TestCase
from _031_lets_go_tochal.lets_go_tochal import get_regular_mountains


class MountainTest(TestCase):
    def test1(self):
        self.assertEqual(get_regular_mountains(4, [1, 4, 3, 1]), 7)
