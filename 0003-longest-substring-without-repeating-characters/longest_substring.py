"""LeetCode 3 · Longest Substring Without Repeating Characters — sliding window.

Keep a window [left, right] and the last index of every character. When the
current character repeats inside the window, jump left past its last index.
Time O(n), space O(min(n, alphabet)).
"""


def length_of_longest_substring_bruteforce(s):
    best = 0
    n = len(s)
    for left in range(n):
        seen = set()
        for right in range(left, n):
            if s[right] in seen:
                break
            seen.add(s[right])
            best = max(best, right - left + 1)
    return best


def length_of_longest_substring(s):
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
