import unittest
import random
import time

import sort


class SortTestCase(unittest.TestCase):

    def generate_cases(self, n=10):
        """
        Generate n random integer sequences.
        """
        for _ in range(n):
            yield [random.randint(0, 100) for _ in range(1000)]

    def setUp(self):
        self.ts = []
        self.n_cases = 10
        self.user_cases = [
            ([0, 5, 3, 2, 2], [0, 2, 2, 3, 5]),
            ([-2, -5, -45], [-45, -5, -2]),
            ([], []),
        ]

    def tearDown(self):
        avg_ms = 1e-6 * sum(self.ts) / self.n_cases
        print(f'Average speed: {avg_ms:.3f}ms')

    def test__python_sort(self):
        for items in self.generate_cases(self.n_cases):
            t1 = time.time_ns()
            sorted(items)
            self.ts.append(time.time_ns() - t1)

    def test__insertion_sort(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.insertion_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)

    def test__selection_sort(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.selection_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)

    def test__selection_sort_recursive(self):
        items = [random.randint(0, 100) for _ in range(10)]
        ans = sorted(items)
        t1 = time.time_ns()
        sort.selection_sort_recursive(items)
        self.ts.append(time.time_ns() - t1)
        self.assertEqual(items, ans)

    def test__bubble_sort(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.bubble_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)

    def test__merge_sort(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            res = sort.merge_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(res, ans)

    def test__quick_sort(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            res = sort.quick_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(res, ans)

    def test__quick_sort_in_place(self):
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.quick_sort_in_place(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)

    def test__shell_sort(self):
        for items, ans in self.user_cases:
            sort.shell_sort(items)
            self.assertEqual(items, ans)
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.shell_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)


    def test__heap_sort(self):
        for items, ans in self.user_cases:
            sort.heap_sort(items)
            self.assertEqual(items, ans)
        for items in self.generate_cases(self.n_cases):
            ans = sorted(items)
            t1 = time.time_ns()
            sort.heap_sort(items)
            self.ts.append(time.time_ns() - t1)
            self.assertEqual(items, ans)
