from unittest import TestCase
from _032_Matrix.matrix import f, g


class MatrixTest(TestCase):
    def test1(self):
        self.assertEqual(90, f([2, 10, 3, 5]))

    def test2(self):
        self.assertEqual(90, g(3, [2, 10, 3, 5]))