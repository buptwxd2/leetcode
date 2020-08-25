class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = []

        def back_tracking(curr_idx, curr_result):
            # nonlocal results

            if curr_idx == len(nums):
                return

            if len(curr_result) > 1:
                results.append(curr_result[:])

            duplicates = set()
            for i in range(curr_idx + 1, len(nums)):
                if nums[i] in duplicates:
                    continue

                duplicates.add(nums[i])
                if nums[i] >= curr_result[-1]:
                    curr_result.append(nums[i])
                    back_tracking(i, curr_result)
                    curr_result.pop(-1)

        duplicates = set()
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                back_tracking(i, [nums[i]])
                duplicates.add(nums[i])

        return results

"""
Results:
回溯问题
Runtime: 232 ms, faster than 87.15% of Python3 online submissions for Increasing Subsequences.
Memory Usage: 21.4 MB, less than 75.55% of Python3 online submissions for Increasing Subsequences.
"""