class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [[], nums]

        nums.sort()
        final = nums[-1]
        sub_results = self.subsetsWithDup(nums[:-1])
        additional_results = [sub_result + [final] for sub_result in sub_results]

        final_results = []
        for result in sub_results + additional_results:
            if result not in final_results:
                final_results.append(result)
        return final_results

"""
Results:
Runtime: 56 ms, faster than 9.14% of Python3 online submissions for Subsets II.
Memory Usage: 14.2 MB, less than 6.38% of Python3 online submissions for Subsets II.
"""