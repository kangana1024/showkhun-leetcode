import unittest

from best_time_to_buy_and_sell_stock import max_profit, max_profit_bruteforce


class StockTests(unittest.TestCase):
    def test_examples_and_edges(self):
        cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([2], 0),
            ([2, 2, 2], 0),
        ]
        for prices, expected in cases:
            with self.subTest(prices=prices):
                self.assertEqual(max_profit(prices), expected)
                self.assertEqual(max_profit(prices), max_profit_bruteforce(prices))


if __name__ == "__main__":
    unittest.main()
