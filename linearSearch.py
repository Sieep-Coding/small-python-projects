class Solution:
    def linearSearch(self, haystack: list[int], needle: int) -> bool:
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return True
            return False
            

import unittest

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        solution = Solution()
        self.assertFalse(solution.linearSearch([1, 2, 3, 4, 5], 3))  # Needle exists
        self.assertFalse(solution.linearSearch([1, 2, 3, 4, 5], 6))  # Needle doesn't exist
        self.assertTrue(solution.linearSearch([1, 2, 3, 4, 5], 1))  # Needle exists at the beginning
        self.assertFalse(solution.linearSearch([1, 2, 3, 4, 5], 5))  # Needle exists at the end
        self.assertFalse(solution.linearSearch([], 3))  # Empty list

if __name__ == '__main__':
    unittest.main()