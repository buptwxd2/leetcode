class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        row = col = len(s)

        matrix = [[0] * col for _ in range(row)]

        cnt = 0

        for j in range(col):
            for i in range(j + 1):
                if i == j:
                    matrix[i][j] = 1
                    cnt += 1

                elif j - i == 1 and s[i] == s[j]:
                    matrix[i][j] = 1
                    cnt += 1

                elif matrix[i + 1][j - 1] == 1 and s[i] == s[j]:
                    matrix[i][j] = 1
                    cnt += 1

        return cnt

"""
Results:
Runtime: 284 ms, faster than 42.31% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 21.5 MB, less than 24.68% of Python3 online submissions for Palindromic Substrings.
"""