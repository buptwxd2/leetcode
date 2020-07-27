class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        i, j = 0, 0

        while i < m and j < n:
            if t[j] == s[i]:
                j += 1
                i += 1
            else:
                j += 1

        return i == m

"""
Results:
双指针
Runtime: 36 ms, faster than 62.16% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.8 MB, less than 77.81% of Python3 online submissions for Is Subsequence.
"""