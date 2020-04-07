class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_num = len(prices)

        if total_num == 0 or total_num == 1:
            return 0

        positive_deltas = []

        for i in range(1, total_num):
            if prices[i] - prices[i - 1] > 0:
                positive_deltas.append(prices[i] - prices[i - 1])

        return sum(positive_deltas)


"""
Results:
Runtime: 56 ms, faster than 92.61% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.1 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""