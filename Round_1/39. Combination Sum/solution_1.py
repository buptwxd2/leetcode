class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def back_tracking(tmp_result, candidates):
            if sum(tmp_result) > target:
                return

            if sum(tmp_result) == target:
                result = sorted(tmp_result)
                if result not in results:
                    results.append(result)

                return

            for i in candidates:
                tmp_result.append(i)
                back_tracking(tmp_result, candidates)
                tmp_result.pop(-1)

        back_tracking([], candidates)

        return results

"""
Results:
Back Tracking -> Try using DP way
Runtime: 748 ms, faster than 5.04% of Python3 online submissions for Combination Sum.
Memory Usage: 13.9 MB, less than 50.92% of Python3 online submissions for Combination Sum.
"""