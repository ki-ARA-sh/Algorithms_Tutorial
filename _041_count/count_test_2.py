from unittest import TestCase
from _041_count.count_2 import count_k


class CountTest(TestCase):
    def test1(self):
        a = [2, -2, 3]
        n = 3
        k = 2
        self.assertEqual(2, count_k(a, n, k))

    def test2(self):
        a = [2, -3, 0, 3, 2]
        n = 5
        k = 0
        self.assertEqual(13, count_k(a, n, k))

    def test3(self):
        a = [-1, 4, -5, 6]
        n = 4
        k = 0
        self.assertEqual(10, count_k(a, n, k))