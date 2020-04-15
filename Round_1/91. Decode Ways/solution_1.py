class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        num = self.numDecodings(s[1:])
        if int(s[0:2]) <= 26:
            num += self.numDecodings(s[2:])

        return num

s = Solution()
s.numDecodings('12')