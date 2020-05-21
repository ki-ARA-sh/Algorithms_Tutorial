from unittest import TestCase
from _028_knapsack.knapsack import knapsack_dp, knapsack_recursive


class  knapsack_test(TestCase):
    w = [12, 2, 1, 1, 4]
    v = [4, 2, 1, 2, 10]
    s = 11
    n = 5
    def test_recursive(self):
        self.assertEqual(knapsack_recursive(self.w, self.v, self.n, self.s), 15)

    def test_dp(self):
        self.assertEqual(knapsack_dp(self.w, self.v, self.n, self.s), 15)
