class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def back_track(tmp_result, choices):
            nonlocal results

            if sum(tmp_result) == target:
                tmp_result = sorted(tmp_result)
                if tmp_result not in results:
                    results.append(tmp_result)

                return

            if sum(tmp_result) > target:
                return

            for idx, num in enumerate(choices):
                tmp_result.append(num)
                back_track(tmp_result, choices[idx + 1:])
                tmp_result.pop(-1)

        back_track([], candidates)

        return results

"""
Results:
Back Tracking Algorithm
Runtime: 284 ms, faster than 18.86% of Python3 online submissions for Combination Sum II.
Memory Usage: 14.1 MB, less than 8.41% of Python3 online submissions for Combination Sum II.
"""