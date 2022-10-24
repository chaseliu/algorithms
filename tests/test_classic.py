import unittest

from classic import hanoi, longest_mountain


class HanoiTestCase(unittest.TestCase):

    def test__hanoi_with_2_disks(self):
        steps = hanoi(2)
        self.assertEqual(len(steps), 3)

    def test__hanoi_with_3_disks(self):
        steps = hanoi(3)
        self.assertEqual(len(steps), 7)


class LongestMountainTestCase(unittest.TestCase):

    def test__longest_mountain(self):
        ans = longest_mountain([2, 1, 4, 7, 3, 2, 5])
        self.assertEqual(ans, 5)
