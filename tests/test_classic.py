import unittest

from classic import hanoi, n_queens


class HanoiTestCase(unittest.TestCase):

    def test__hanoi_with_2_disks(self):
        steps = hanoi(2)
        self.assertEqual(len(steps), 3)

    def test__hanoi_with_3_disks(self):
        steps = hanoi(3)
        self.assertEqual(len(steps), 7)


class QueenTestCase(unittest.TestCase):

    def test__eight_queens(self):
        solves = n_queens(8)
        print(solves)
        self.assertEqual(len(solves), 92)
