from unittest import TestCase
from _028_knapsack.knapsack import knapsack_dp, knapsack_recursive, knapsack_exact_recursive, \
    knapsack_exact_dp, knapsack_dp_optimized_memory


class KnapsackTest(TestCase):
    w = [12, 2, 1, 1, 4]
    v = [4, 2, 1, 2, 10]
    s = 11
    n = 5
    req_output = 15

    def test_recursive(self):
        self.assertEqual(knapsack_recursive(self.w, self.v, self.n, self.s), self.req_output)

    def test_dp(self):
        self.assertEqual(knapsack_dp(self.w, self.v, self.n, self.s), self.req_output)

    def test_dp_optimized_memory(self):
        self.assertEqual(knapsack_dp_optimized_memory(self.w, self.v, self.n, self.s), self.req_output)

    def test_exact(self):
        self.assertEqual(knapsack_exact_recursive([1, 2, 3, 4, 5], 5, 5), 3)

    def test_exact_dp(self):
        self.assertEqual(knapsack_exact_dp([1, 2, 3, 4, 5], 5, 5), 3)

