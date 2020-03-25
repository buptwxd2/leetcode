class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0

        length = len(nums)

        dp_positive = [0] * length
        dp_negative = [0] * length

        # initialize the first element
        dp_positive[0] = dp_negative[0] = nums[0]

        for i in range(1, length):
            if nums[i] >= 0:
                dp_positive[i] = max(nums[i], nums[i] * dp_positive[i-1])
                dp_negative[i] = min(nums[i], nums[i] * dp_negative[i-1])
            else:
                dp_positive[i] = max(nums[i], nums[i] * dp_negative[i-1])
                dp_negative[i] = min(nums[i], nums[i] * dp_positive[i-1])

        return max(dp_positive)

s = Solution()
print(s.maxProduct([-4,-3,-2]))

"""
Results:
Runtime: 56 ms, faster than 60.39% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.2 MB, less than 17.24% of Python3 online submissions for Maximum Product Subarray.
"""