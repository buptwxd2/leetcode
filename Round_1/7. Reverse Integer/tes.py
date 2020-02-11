class Solution:
    def firstUniqChar(self, s: str) -> int:
        strset = set(s)
        d = {}
        for i in strset:
            d[i] = s.count(i)
        for j in range(len(s)):
            if d[s[j]] == 1:
                return j
        return -1