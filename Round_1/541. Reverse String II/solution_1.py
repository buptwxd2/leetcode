class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        length = len(s)

        pair_num = length // (2 * k)
        remaining = length % (2 * k)

        for i in range(pair_num):
            for j in range(k//2):
                s[i*2*k+j], s[i*2*k+k-1-j] = s[i*2*k+k-1-j], s[i*2*k+j]

        if remaining < k:
            for j in range(remaining//2):
                s[length-remaining+j], s[length-remaining+remaining-1-j] = s[length-remaining+remaining-1-j], s[length-remaining+j]
        elif remaining:
            for j in range(k//2):
                s[length-remaining+j], s[length-remaining+k-1-j] = s[length-remaining+k-1-j], s[length-remaining+j]

        return ''.join(s)


s = Solution()
x = s.reverseStr("abcdefg", 8)
print(x)