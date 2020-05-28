from unittest import TestCase
from _033_combo_number.combo_number import f


class ComboTest(TestCase):
    def test1(self):
        self.assertEqual(2, f(3, 2))

    def test2(self):
        self.assertEqual(5, f(4, 2))
