import unittest

from queens.n_queens import n_queens_01, n_queens_02


class QueenTestCase(unittest.TestCase):

    def test__n_queens_01(self):
        solves = n_queens_01(8)
        print(solves)
        self.assertEqual(len(solves), 92)

    def test__n_queens_02(self):
        solves = n_queens_02(8)
        print(solves)
        self.assertEqual(len(solves), 92)
