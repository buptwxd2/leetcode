class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []
        length = len(nums)

        def back_track(tmp_result):
            if len(tmp_result) == length:
                results.append(tmp_result[:])

                return

            for num in nums:
                if num in tmp_result:
                    continue

                tmp_result.append(num)
                back_track(tmp_result)
                tmp_result.pop(-1)

        back_track([])

        return results

"""
Results:
Runtime: 36 ms, faster than 89.51% of Python3 online submissions for Permutations.
Memory Usage: 14.4 MB, less than 5.05% of Python3 online submissions for Permutations.
"""