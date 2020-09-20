class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        results = []

        def back_track(tmp_result, remaining_choices):
            if len(tmp_result) == k:
                results.append(tmp_result[:])

                return

            for idx, num in enumerate(remaining_choices):
                # Choose it
                tmp_result.append(num)
                back_track(tmp_result, remaining_choices[idx + 1:])
                tmp_result.pop(-1)

                # 不能加这一块，否则结果会重复
                # # NOT choose it
                # back_track(tmp_copy_2, remaining_choices[idx+1:])

        back_track([], list(range(1, n + 1)))

        return results

"""
Results:
Runtime: 600 ms, faster than 39.56% of Python3 online submissions for Combinations.
Memory Usage: 15.3 MB, less than 28.29% of Python3 online submissions for Combinations.
"""