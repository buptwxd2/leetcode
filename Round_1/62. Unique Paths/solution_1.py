class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp way

        dp = [[None] * n for _ in range(m)]

        # initialize the first row
        for j in range(n):
            dp[0][j] = 1

        # initialize the first column
        for i in range(m):
            dp[i][0] = 1

        # dp move forward
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]

"""
Results:
Runtime: 28 ms, faster than 87.97% of Python3 online submissions for Unique Paths.
Memory Usage: 13.6 MB, less than 96.13% of Python3 online submissions for Unique Paths.
"""