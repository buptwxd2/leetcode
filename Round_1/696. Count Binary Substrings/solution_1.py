class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnts = []

        i = 0
        while i < len(s):
            c = s[i]
            count = 0

            while i < len(s) and s[i] == c:
                i += 1
                count += 1

            cnts.append(count)

        result = 0
        for i in range(len(cnts) - 1):
            tmp = min(cnts[i], cnts[i + 1])
            result += tmp

        return result

"""
Results:
Runtime: 268 ms, faster than 27.76% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 14.4 MB, less than 31.98% of Python3 online submissions for Count Binary Substrings.
"""