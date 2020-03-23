class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # for amount 0, result is 0

        for coin in coins:
            for x in range(coin, amount + 1):
                if dp[x - coin] + 1 < dp[x]:
                    dp[x] = dp[x - coin] + 1

        return dp[-1] if dp[-1] < float('inf') else -1


s = Solution()
print(s.coinChange([2, 5, 43, 55, 70], 188))


"""
Results:
Runtime: 752 ms, faster than 92.58% of Python3 online submissions for Coin Change.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Coin Change.
"""