class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, buy_p in enumerate(prices[:-1]):
            for j, sell_p in enumerate(prices[i + 1:]):
                delta = sell_p - buy_p
                if delta > profit:
                    profit = delta

        return profit

"""
Results: Time Exceeded. O(n ** 2)
"""