from unittest import TestCase
from _047_classy_startup.classy_startup import count_chocolates


class StartupTest(TestCase):
    def test1(self):
        self.assertListEqual([1, 1, 0, 0], count_chocolates([3, 2, 1, 3]))

    def test2(self):
        self.assertListEqual([2, 1, 1, 1], count_chocolates([3, 3, 5, 3]))

    def test3(self):
        self.assertListEqual([2, 2, 2, 1], count_chocolates([4, 2, 5, 3]))