class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])

        return dp[-1]


"""
Results:
DP way
Runtime: 40 ms, faster than 42.45% of Python3 online submissions for Integer Break.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Integer Break
"""