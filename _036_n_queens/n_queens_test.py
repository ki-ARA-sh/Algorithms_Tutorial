from unittest import TestCase
from _036_n_queens.n_queens import n_queens


class NQueensTest(TestCase):
    def test1(self):
        n = 3
        k = 2
        board = [[0 for i in range(n)] for j in range(n)]
        self.assertEqual(8, n_queens(0, n, board, k))

    def test2(self):
        n = 4
        k = 4
        board = [[0 for i in range(n)] for j in range(n)]
        self.assertEqual(2, n_queens(0, n, board, k))
