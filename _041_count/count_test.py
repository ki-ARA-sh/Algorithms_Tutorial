from unittest import TestCase
from _041_count.count import count_k, get_ps, count_k_2


class CountTest(TestCase):
    def test1(self):
        a = [2, -2, 3]
        n = 3
        ps = get_ps(a, n)
        k = 2
        self.assertEqual(2, count_k_2(ps, n, k))

    def test2(self):
        a = [2, -3, 0, 3, 2]
        n = 5
        ps = get_ps(a, n)
        k = 0
        self.assertEqual(13, count_k_2(ps, n, k))


