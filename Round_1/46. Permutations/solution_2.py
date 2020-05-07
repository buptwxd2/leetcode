# Use back tracing

class Solution:
    def permute(self, nums):
        results = []

        def back_tracing(curr_result, remaining_list):
            if not remaining_list:
                results.append(curr_result)
                return

            for num in remaining_list:
                # here is the key; backup curr_result and remaining_list first; then modify them
                tmp_result = curr_result[:]
                tmp_remaining_list = remaining_list[:]

                tmp_result.append(num)
                tmp_remaining_list.remove(num)
                back_tracing(tmp_result, tmp_remaining_list)

        back_tracing([], nums)

        return results

"""
Results:
Runtime: 36 ms, faster than 87.68% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.
"""