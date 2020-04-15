class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        return sum(sorted_nums[0::2])


"""
Results:
Runtime: 272 ms, faster than 97.76% of Python3 online submissions for Array Partition I.
Memory Usage: 16.3 MB, less than 6.06% of Python3 online submissions for Array Partition I.
"""