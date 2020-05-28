
from unittest import TestCase
from _034_backslap_sequence.backslap_sequence import f


class BackslapTest(TestCase):
    def test1(self):
        self.assertEqual(11, f([{1, 2, 3}, {1, 2, 4}, {4, 5}], set()))

    def test2(self):
        self.assertEqual(11, f([[1, 2, 3], [1, 2, 4], [4, 5]], list()))