class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums:
            if num in my_set:
                return num
            else:
                my_set.add(num)

"""
Results:
Runtime: 64 ms, faster than 83.75% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 17.9 MB, less than 7.14% of Python3 online submissions for Find the Duplicate Number.
"""