class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        if size == 0 or size == 1:
            return 0

        deltas = []

        for i in range(1, size):
            delta = prices[i] - prices[i - 1]
            deltas.append(delta)

        # convert to problem 53. Maximum Subarray
        # f(i) = max(f[i-1] + nums[i], nums[i])
        # Or f(i) = f(i-1) + nums[i] if f(i-1) > 0 else: nums[i]

        # use method_1: f(i) = max(f[i-1] + nums[i], nums[i])
        # see solution_5 for the second method
        max_current = global_current = deltas[0]
        for i in range(1, len(deltas)):
            max_current = max(max_current + deltas[i], deltas[i])
            if max_current > global_current:
                global_current = max_current

        return max(0, global_current)

"""
Results:
Runtime: 64 ms, faster than 61.76% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 90.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""