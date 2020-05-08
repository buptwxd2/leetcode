# back tracing
# sorting nums first and skip the iteration if duplicated

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_tracing(curr_result, nums):
            if not nums:
                if curr_result not in results:
                    results.append(curr_result)

                return

            for i, num in enumerate(nums):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue

                curr_result_copy = curr_result[:]
                nums_copy = nums[:]

                curr_result_copy.append(num)
                nums_copy.remove(num)

                back_tracing(curr_result_copy, nums_copy)

        nums.sort()
        back_tracing([], nums)

        return results

"""
Results:
Runtime: 80 ms, faster than 37.61% of Python3 online submissions for Permutations II.
Memory Usage: 13.9 MB, less than 8.89% of Python3 online submissions for Permutations II.
"""