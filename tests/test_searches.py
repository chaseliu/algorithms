import unittest
import random
import time

import searches


class SearchTestCase(unittest.TestCase):

    def generate_cases(self, n=10):
        """
        Generate n random integer sequences.
        """
        for _ in range(n):
            yield [random.randint(0, 100) for _ in range(10)]

    def setUp(self):
        self.n_cases = 10
        self.user_cases = [
            ([1, 1, 1, 1, 3], 1, 0),
            ([0, 1, 2, 3, 4], 4, 4),
            ([0, 3, 5, 6, 7], 3, 1),
            ([0, 0, 0], -2, -1),
            ([0, 0, 0], 2, -1),
            ([], 1, -1),
        ]

    def test__interpolation_search(self):
        for case in self.user_cases:
            arr, item, ans = case
            self.assertEqual(searches.interpolation_search(arr, item), ans)
        for case in self.generate_cases(self.n_cases):
            arr = sorted(case)
            item = arr[random.randint(0, len(arr) - 1)]
            print(arr, item)
            self.assertEqual(searches.interpolation_search(
                arr, item), arr.index(item))
