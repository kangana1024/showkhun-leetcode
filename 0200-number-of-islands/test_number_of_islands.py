import unittest

from number_of_islands import islands_bfs, islands_dfs


class NumberOfIslandsTests(unittest.TestCase):
    def test_examples_and_edges(self):
        cases = [([], 0), ([["0"]], 0), ([["1"]], 1),
                 ([list("11000"), list("11000"), list("00100"), list("00011")], 3)]
        for grid, expected in cases:
            self.assertEqual(islands_dfs([row[:] for row in grid]), expected)
            self.assertEqual(islands_bfs([row[:] for row in grid]), expected)

    def test_diagonal_does_not_connect(self):
        grid = [list("10"), list("01")]
        self.assertEqual(islands_dfs([row[:] for row in grid]), 2)
        self.assertEqual(islands_bfs([row[:] for row in grid]), 2)


if __name__ == "__main__":
    unittest.main()
