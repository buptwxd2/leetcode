class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        results = []

        def back_tracking(curr_list, remaining_list):
            if len(results) >= k:
                return

            if len(curr_list) == n:
                results.append(curr_list[:])

                return

            for m in remaining_list:
                curr_list.append(m)

                tmp_list = remaining_list[:]
                tmp_list.remove(m)
                back_tracking(curr_list, tmp_list)

                # back tracking
                curr_list.pop(-1)

        back_tracking([], list(range(1, n + 1)))

        return "".join(str(x) for x in results[-1])

"""
Results:
Back Tracking way；But Time Limit Exceeded
"""
