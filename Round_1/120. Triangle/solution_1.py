class Solution:
    def minimumTotal(self, triangle) -> int:
        row = len(triangle)
        column = len(triangle)
        if row == 0:
            return 0

        # dp or states
        dp = [[float('inf')] * column for _ in range(row)]

        # initialize the first row
        dp[0][0] = triangle[0][0]

        # initialize the first column
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]

        for i in range(1, row):
            for j in range(1, i + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[-1])

"""
Results:
Runtime: 60 ms, faster than 67.76% of Python3 online submissions for Triangle.
Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Triangle.
Analysis:
Space Complexity:
O(n * n), so memory usage is high; see solution_2 to reduce the space complexity
"""