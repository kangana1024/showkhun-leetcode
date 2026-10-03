import unittest

from two_sum import two_sum


class TwoSumTests(unittest.TestCase):
    def test_examples(self):
        cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),   # must not pair index 0 with itself
            ([3, 3], 6, [0, 1]),      # equal values at different indices
        ]
        for nums, target, expected in cases:
            with self.subTest(nums=nums, target=target):
                self.assertEqual(two_sum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
