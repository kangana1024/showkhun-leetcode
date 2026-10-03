import unittest

from valid_parentheses import is_valid


class ValidParenthesesTests(unittest.TestCase):
    def test_examples(self):
        cases = [
            ("()", True),
            ("()[]{}", True),
            ("([{}])", True),
            ("(]", False),
            (")(", False),     # counts match but the order is wrong
            ("([)]", False),
            ("((", False),     # stack not empty at the end
            ("", True),
        ]
        for s, expected in cases:
            with self.subTest(s=s):
                self.assertEqual(is_valid(s), expected)


if __name__ == "__main__":
    unittest.main()
