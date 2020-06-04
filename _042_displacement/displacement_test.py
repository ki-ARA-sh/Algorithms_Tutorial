from unittest import TestCase
from _042_displacement.displacement import count_displacements, count_misplacements
from random import randint


class DisplacementTest(TestCase):
    def test1(self):
        self.assertEqual(2, count_displacements([2, 3, 1], 3))

    def test2(self):
        a, x = count_misplacements([2, 3, 1])
        self.assertEqual(2, x)

    def test3(self):
        n = 10
        a = [randint(1, n) for i in range(10)]
        b, x = count_misplacements(a)
        self.assertListEqual(sorted(a), b)

    def test4(self):
        n = 20
        a = [randint(0, n) for i in range(n)]
        b, x = count_misplacements(a)
        y = count_displacements(a, n)
        self.assertEqual(y, x)