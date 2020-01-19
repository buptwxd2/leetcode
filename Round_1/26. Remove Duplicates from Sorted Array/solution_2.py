class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        array_length = len(nums)
        if array_length == 0 or array_length == 1:
            return array_length

        i = 0
        for j in range(1, array_length):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1

## pointer solution with two pointers
## pointer i is the slow pointer
## pointer j is the fast pointer
