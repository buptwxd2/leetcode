class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_max = global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], nums[i] + current_max)
            if current_max > global_max:
                global_max = current_max

        return global_max


"""
Results:
Runtime: 68 ms, faster than 60.32% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 59.35% of Python3 online submissions for Maximum Subarray.
"""