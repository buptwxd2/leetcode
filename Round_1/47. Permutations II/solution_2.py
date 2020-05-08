class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        sub_lists = self.permuteUnique(nums[:-1])
        final = nums[-1]

        results = []
        for sub_list in sub_lists:
            for i in range(0, len(sub_list) + 1):
                tmp_list = sub_list[:]
                tmp_list.insert(i, final)
                if tmp_list not in results:
                    results.append(tmp_list)

        return results

"""
Results:
Runtime: 116 ms, faster than 29.85% of Python3 online submissions for Permutations II.
Memory Usage: 13.9 MB, less than 8.89% of Python3 online submissions for Permutations II.
"""