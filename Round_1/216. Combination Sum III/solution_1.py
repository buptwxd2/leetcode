class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        results = []

        def back_track(tmp_result):
            if len(tmp_result) == k and sum(tmp_result) == n:
                tmp_result = sorted(tmp_result)
                if tmp_result not in results:
                    results.append(tmp_result)

                return

            if len(tmp_result) == k:
                return

            if sum(tmp_result) == n:
                return

            for i in range(1, 10):
                if i in tmp_result:
                    continue

                tmp_result.append(i)
                back_track(tmp_result)
                tmp_result.pop(-1)

        back_track([])

        return results

"""
Results:
Runtime: 1548 ms, faster than 5.09% of Python3 online submissions for Combination Sum III.
Memory Usage: 14.3 MB, less than 5.01% of Python3 online submissions for Combination Sum III.
"""