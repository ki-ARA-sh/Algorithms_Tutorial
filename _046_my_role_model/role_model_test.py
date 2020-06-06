from unittest import TestCase
from _046_my_role_model.role_model import role_models


class RoleModelTest(TestCase):
    def test1(self):
        self.assertListEqual([1, 3, 5], role_models([3, 1, 1, 5, 5, 4, 6]))
