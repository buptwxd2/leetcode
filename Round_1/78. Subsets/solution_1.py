class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_tracing(results, tmp_result, nums, start):
            results.append(tmp_result)

            for i in range(start, len(nums)):
                tmp_result_copy = tmp_result[:]
                tmp_result_copy.append(nums[i])
                back_tracing(results, tmp_result_copy, nums, i + 1)

        back_tracing(results, [], nums, 0)

        return results

"""
Results:
Runtime: 36 ms, faster than 44.98% of Python3 online submissions for Subsets.
Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for Subsets.
"""