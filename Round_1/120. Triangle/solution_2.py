class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)

        if row == 0:
            return 0

        dp = [float('inf')] * row

        # initialize
        dp[0] = triangle[0][0]

        for i in range(1, row):
            for j in range(i, 0, -1):           # key point: we need to back propagate from i to 0
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]

            dp[0] = dp[0] + triangle[i][0]

        return min(dp)

"""
Results:
Runtime: 60 ms, faster than 67.76% of Python3 online submissions for Triangle.
Memory Usage: 13.5 MB, less than 80.00% of Python3 online submissions for Triangle.
Space Complexity:
O(n), so memory usage is low
"""