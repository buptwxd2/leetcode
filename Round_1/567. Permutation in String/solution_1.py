class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def cal_permutations(str_list):
            results = []

            length = len(str_list)

            def back_track(tmp_result, choices):
                if len(tmp_result) == length:
                    results.append("".join(tmp_result))

                    return

                for i, char in enumerate(choices):
                    if i > 0 and str_list[i] == str_list[i - 1]:
                        continue

                    tmp_result.append(char)
                    choices_cp = choices[:]
                    choices_cp.remove(char)
                    back_track(tmp_result, choices_cp)
                    tmp_result.pop(-1)

            back_track([], str_list)

            return results

        str_list = sorted(s1)

        s1_permutations = cal_permutations(str_list)

        for s1_permutation in s1_permutations:
            if s1_permutation in s2:
                return True

        return False

"""
Results:
Time Limit Exceeded
"""