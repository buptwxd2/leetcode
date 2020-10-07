class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length == 0 or length == 1:
            return

        first = 0  # left of first pointer is all 0
        last = length - 1  # right of last pointer is all 2

        while first < length and nums[first] == 0:
            first += 1

        while last > -1 and nums[last] == 2:
            last -= 1

        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        idx = first
        while idx <= last:
            if nums[idx] == 0:
                swap(nums, idx, first)
                first += 1
                idx += 1

            elif nums[idx] == 1:
                idx += 1

            else:
                swap(nums, idx, last)
                last -= 1

        return

"""
Results:
Refer to https://www.youtube.com/watch?v=J9DgvL6L1nk
Runtime: 28 ms, faster than 91.89% of Python3 online submissions for Sort Colors.
Memory Usage: 14.2 MB, less than 5.09% of Python3 online submissions for Sort Colors.
"""