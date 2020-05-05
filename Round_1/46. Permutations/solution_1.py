class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        final = nums[-1]
        sub_results = self.permute(nums[:-1])

        results = []
        for sub_list in sub_results:
            for i in range(0, len(sub_list) + 1):
                tmp_list = sub_list[:]
                tmp_list.insert(i, final)
                results.append(tmp_list)

        return results

"""
Results:
Runtime: 32 ms, faster than 96.63% of Python3 online submissions for Permutations.
Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Permutations.
"""