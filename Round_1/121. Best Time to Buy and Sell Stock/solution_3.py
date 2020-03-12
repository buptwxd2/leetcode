class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        low_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < low_price:
                low_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - low_price)

        return max_profit


s = Solution()
s.maxProfit([7,1,5,3,6,4])

"""
Results:
Runtime: 64 ms, faster than 61.76% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 70.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""