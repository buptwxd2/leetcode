class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for i, idx in enumerate(index):
            result.insert(idx, nums[i])

        return result

"""
Results
Runtime: 36 ms, faster than 47.32% of Python3 online submissions for Create Target Array in the Given Order.
Memory Usage: 14.2 MB, less than 5.22% of Python3 online submissions for Create Target Array in the Given Order.
"""