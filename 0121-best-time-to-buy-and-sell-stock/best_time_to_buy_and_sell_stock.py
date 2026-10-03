"""LeetCode 121 · Best Time to Buy and Sell Stock — track the lowest price.

Remember the lowest price seen so far and ask every day how much selling
today would earn. Time O(n), space O(1).
"""


def max_profit(prices):
    lowest = float("inf")
    best = 0
    for price in prices:
        best = max(best, price - lowest)
        lowest = min(lowest, price)
    return best


def max_profit_bruteforce(prices):
    return max(
        0,
        max(
            (prices[j] - prices[i] for i in range(len(prices))
             for j in range(i + 1, len(prices))),
            default=0,
        ),
    )
