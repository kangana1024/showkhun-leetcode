import unittest

from longest_substring import length_of_longest_substring, length_of_longest_substring_bruteforce


class LongestSubstringTests(unittest.TestCase):
    def test_examples(self):
        cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("au", 2),
            ("dvdf", 3),   # the repeat must be inside the window before left jumps
        ]
        for s, expected in cases:
            with self.subTest(s=s):
                self.assertEqual(length_of_longest_substring(s), expected)
                self.assertEqual(length_of_longest_substring_bruteforce(s), expected)

    def test_unicode_and_space(self):
        self.assertEqual(length_of_longest_substring("a b a"), 3)


if __name__ == "__main__":
    unittest.main()
