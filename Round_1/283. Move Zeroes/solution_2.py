class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = fast = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        for i in range(slow, len(nums)):
            nums[i] = 0

        return

"""
Results:
快慢指针
Runtime: 52 ms, faster than 60.86% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 5.15% of Python3 online submissions for Move Zeroes.
"""