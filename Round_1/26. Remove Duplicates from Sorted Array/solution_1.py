class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        array_length = len(nums)
        if array_length == 0 or array_length == 1:
            return array_length

        pre_num = nums[0]
        for num in nums[1:]:
            if num == pre_num:
                nums.remove(num)
            else:
                pre_num = num

        return len(nums)