class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in set(t):
            if s.count(char) != t.count(char):
                return char


"""
Results:
Runtime: 20 ms, faster than 99.53% of Python3 online submissions for Find the Difference.
Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Find the Difference.
"""