class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [[], nums]

        final = nums[-1]
        sub_results = self.subsets(nums[:-1])
        additioanl_results = [sub_result + [final] for sub_result in sub_results]

        return sub_results + additioanl_results

"""
Results:
Runtime: 32 ms, faster than 74.94% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 5.95% of Python3 online submissions for Subsets.
"""