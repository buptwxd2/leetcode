class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_tracing(curr_result, nums):
            if not nums:
                results.append(curr_result)

                return


            for num in list(set(nums)):
                curr_result_copy = curr_result[:]
                nums_copy = nums[:]

                curr_result_copy.append(num)
                nums_copy.remove(num)

                back_tracing(curr_result_copy, nums_copy)

        back_tracing([], nums)

        return results

"""
Results:
Runtime: 48 ms, faster than 95.67% of Python3 online submissions for Permutations II.
Memory Usage: 14.2 MB, less than 6.67% of Python3 online submissions for Permutations II.
"""