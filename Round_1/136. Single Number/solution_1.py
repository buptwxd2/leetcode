class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_set = set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                my_set.remove(num)

        assert len(my_set) == 1, "Unexpected num list"

        return my_set.pop()