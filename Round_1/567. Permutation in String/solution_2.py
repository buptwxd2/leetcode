class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def cal_char_cnt(s):
            chars = set(s)

            my_dict = {}
            for char in chars:
                my_dict[char] = s.count(char)

            return my_dict

        target_dict = cal_char_cnt(s1)

        l1 = len(s1)
        l2 = len(s2)

        for i in range(l2 - l1 + 1):
            sub_s = s2[i: i + l1]
            sub_s_dict = cal_char_cnt(sub_s)
            if target_dict == sub_s_dict:
                return True

        return False

"""
Results:
Sliding window(滑动窗口)
Runtime: 1276 ms, faster than 23.97% of Python3 online submissions for Permutation in String.
Memory Usage: 14.3 MB, less than 5.00% of Python3 online submissions for Permutation in String.
"""