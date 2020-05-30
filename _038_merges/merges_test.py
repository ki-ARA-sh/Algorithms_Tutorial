from unittest import TestCase
from _038_merges.merges import merges, merges_divided


class MergesTest(TestCase):
    def test1(self):
        self.assertListEqual([1, 4, 4, 4, 8, 100], merges_divided([[1, 4, 100], [4, 4, 8]]))
