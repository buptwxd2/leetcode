class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        import math
        states = [[math.inf] * (amount + 1) for _ in range(amount)]

        # initialie the first row
        for coin in coins:
            if coin <= amount:
                states[0][coin] = 1

        # iterate to the next row using dp way
        for i in range(1, amount):
            for j in range(1, amount + 1):
                if states[i - 1][j] < math.inf:
                    for coin in coins:
                        if j + coin <= amount:
                            if states[i - 1][j] + 1 < states[i][j + coin]:
                                states[i][j + coin] = states[i - 1][j] + 1

        for i in range(amount):
            if states[i][amount] < math.inf:
                return states[i][amount]

        return -1

s = Solution()
print(s.coinChange([3,7,405,436], 8839))


"""
Results:
Time Limit Exceeded
"""