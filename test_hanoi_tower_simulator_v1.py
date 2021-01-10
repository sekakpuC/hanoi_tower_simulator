from unittest import TestCase

from hanoi_tower_simulator_v1 import get_extra_bar


class Test(TestCase):
    def test_get_extra_bar(self):
        self.assertEqual(1, get_extra_bar(0, 2))
        self.assertEqual(1, get_extra_bar(2, 0))
        self.assertEqual(2, get_extra_bar(0, 1))
        self.assertEqual(2, get_extra_bar(1, 0))
        self.assertEqual(0, get_extra_bar(1, 2))
        self.assertEqual(0, get_extra_bar(2, 1))
