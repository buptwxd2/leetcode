class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        for j, num in enumerate(nums):
            if num == val:
                continue

            nums[i] = num
            i += 1

        return i