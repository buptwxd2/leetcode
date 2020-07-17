class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = low + 1

        return low

"""
Results:
Binary Search 二分查找
Runtime: 68 ms, faster than 34.86% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.5 MB, less than 45.46% of Python3 online submissions for Search Insert Position.
"""