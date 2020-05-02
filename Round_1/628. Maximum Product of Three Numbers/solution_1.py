class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_p = float('-inf')

        nums = sorted(nums)

        return max(nums[0] * nums[1] * nums[-1],
                   nums[-3] * nums[-2] * nums[-1])

"""
Results:
Runtime: 272 ms, faster than 79.75% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 14.7 MB, less than 6.67% of Python3 online submissions for Maximum Product of Three Numbers.
"""