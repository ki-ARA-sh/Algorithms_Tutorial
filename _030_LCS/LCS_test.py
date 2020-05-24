from unittest import TestCase
from _030_LCS.LCS import lcs


class LcsTest(TestCase):

    def test1(self):
        self.assertSequenceEqual(lcs("katana", "yektaneh"), (4, "ktan"))

    def test2(self):
        self.assertSequenceEqual(lcs("kamid", "komod"), (3, "kmd"))

    # def lcs_test_1(self):
    #     self.assertSequenceEqual(lcs("katana", "yektaneh"), (4, "ktan"))
    #
    # def lcs_test_2(self):
    #     self.assertSequenceEqual(lcs("kamid", "komod"), (3, "kmd"))
