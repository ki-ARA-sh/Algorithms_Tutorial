from unittest import TestCase
from _039_power_function.power_function import power_function


class PowerFunctionTest(TestCase):
    def test1(self):
        self.assertEqual('1.000', power_function(1, 100))

    def test2(self):
        self.assertEqual('1667.988', power_function(2.1, 10))
