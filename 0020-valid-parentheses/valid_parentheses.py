"""LeetCode 20 · Valid Parentheses — stack.

Push every opening bracket. On a closing bracket the top of the stack
must be its partner, then pop. The string is valid when the stack ends empty.
Time O(n), space O(n).
"""


def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
