class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * len(nums)

        length = len(nums)

        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return max(nums)

        #
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

"""
Results:
DP Algorithm
Runtime: 32 ms, faster than 69.51% of Python3 online submissions for House Robber.
Memory Usage: 14.1 MB, less than 7.02% of Python3 online submissions for House Robber.
"""