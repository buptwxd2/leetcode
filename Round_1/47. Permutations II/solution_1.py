class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_tracing(curr_result, nums):
            if not nums:
                if curr_result not in results:
                    results.append(curr_result)

                return

            for num in nums:
                curr_result_copy = curr_result[:]
                nums_copy = nums[:]

                curr_result_copy.append(num)
                nums_copy.remove(num)

                back_tracing(curr_result_copy, nums_copy)

        back_tracing([], nums)

        return results

"""
Results:
Runtime: 1388 ms, faster than 7.38% of Python3 online submissions for Permutations II.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Permutations II.
"""