class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


"""
Results:
Runtime: 24 ms, faster than 83.95% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""