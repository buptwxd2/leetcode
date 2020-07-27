class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if m > n:
            return False

        if n == 0:
            return m == 0

        if m == 0:
            return True

        i, j = 0, 0

        while i < m:
            found = False  # indicate whether s[i] is found in t

            while j < n:
                if t[j] == s[i]:
                    found = True
                    break
                else:
                    j += 1

            if not found:
                return False
            else:
                i += 1
                j += 1

        return True

"""
Results:
双指针解决
Runtime: 32 ms, faster than 79.54% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.1 MB, less than 22.99% of Python3 online submissions for Is Subsequence.
"""