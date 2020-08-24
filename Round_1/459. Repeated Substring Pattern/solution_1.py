class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for sub_s_len in range(1, len(s) // 2 + 1):

            if len(s) % sub_s_len != 0:
                continue

            # check if satisfied
            pattern = s[:sub_s_len]

            for idx in range(sub_s_len, len(s), sub_s_len):
                sub_s = s[idx: idx + sub_s_len]
                if sub_s != pattern:
                    break
            else:
                return True

        return False

"""
Results:
Runtime: 56 ms, faster than 72.11% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 13.7 MB, less than 92.37% of Python3 online submissions for Repeated Substring Pattern.
"""