"""LeetCode 1 · Two Sum — one-pass hash map.

Walk the array once. For each value, ask whether its partner
(target - value) was already seen; if so, return both indices.
Time O(n), space O(n).
"""


def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], i]
        seen[value] = i
