class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        for coin in coins:
            if amount == coin:
                return 1

        candidates = []
        for coin in coins:
            if self.coinChange(coins, amount - coin) != -1:
                candidates.append(self.coinChange(coins, amount - coin))

        if not candidates:
            return -1
        else:
            return min(candidates) + 1


s = Solution()
print(s.coinChange([2], 3))

"""
Results:
Time Limit Exceeded
"""