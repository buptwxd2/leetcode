class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_num = len(prices)

        if total_num == 0 or total_num == 1:
            return 0

        # change to list comprehension
        positive_deltas = [prices[i] - prices[i - 1] for i in range(1, total_num) if prices[i] - prices[i - 1] > 0]

        return sum(positive_deltas)


"""
Results:
Runtime: 48 ms, faster than 99.71% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""