class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        results = []
        length = len(S)

        def back_track(tmp_result, index):
            if index == length:
                results.append(tmp_result)

                return

            if S[index].isalpha():
                back_track(tmp_result + S[index].lower(), index + 1)
                back_track(tmp_result + S[index].upper(), index + 1)
            else:
                back_track(tmp_result + S[index], index + 1)

        back_track('', 0)

        return results

"""
Results:
Back Tracking Algorithm
Runtime: 60 ms, faster than 64.83% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.3 MB, less than 8.31% of Python3 online submissions for Letter Case Permutation.
"""