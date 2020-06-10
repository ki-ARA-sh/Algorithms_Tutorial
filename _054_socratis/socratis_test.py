from unittest import TestCase
from _054_socratis.socratis import assignment


class AssignmentTest(TestCase):
    def test1(self):
        ans, cost = assignment(4, [0, 1, 2, 3], [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]])
        self.assertListEqual([1, 0, 2, 3], ans)