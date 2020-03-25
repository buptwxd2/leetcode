class Solution:
    def maxProduct(self, nums) -> int:
        current_max, current_min, gloal_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            current_max, current_min = max(nums[i], nums[i] * current_max, nums[i] * current_min), min(nums[i] , nums[i] * current_max, nums[i] * current_min)

            if current_max > gloal_max:
                gloal_max = current_max

        return gloal_max

"""
Results:
Runtime: 44 ms, faster than 98.60% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 13.2 MB, less than 93.10% of Python3 online submissions for Maximum Product Subarray.
"""