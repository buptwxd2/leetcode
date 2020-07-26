class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[float('inf')] * col for _ in range(row)]

        # initialize
        dp[0][0] = grid[0][0]

        # initialize the first row
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # initialize the first column
        for j in range(1, row):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        # dp way to move forward
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]

"""
Classical DP problem
Runtime: 124 ms, faster than 40.80% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.3 MB, less than 68.25% of Python3 online submissions for Minimum Path Sum.
"""