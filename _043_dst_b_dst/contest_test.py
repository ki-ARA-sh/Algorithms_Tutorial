from unittest import TestCase
from _043_dst_b_dst.contest import f


class ContestTest(TestCase):
    def test1(self):
        a = list(map(int, '1 2 3 4'.split()))
        n = 2
        self.assertEqual(9, f(a, n))

    def test2(self):
        a = list(map(int, '1 6 1 7 1 8 1 4'.split()))
        n = 3
        self.assertEqual(22, f(a, n))