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

        # use the method_2: f(i) = f(i-1) + nums[i] if f(i-1) > 0 else: nums[i]
        max_list = [deltas[0]]
        for i in range(1, len(deltas)):
            max_ending_i = deltas[i] if max_list[i - 1] <= 0 else deltas[i] + max_list[i - 1]
            max_list.append(max_ending_i)

        return max(0, max(max_list))


"""
Results:
Runtime: 60 ms, faster than 83.40% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14 MB, less than 34.48% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""