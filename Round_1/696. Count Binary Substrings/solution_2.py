class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def is_valid(s, start, end):
            if s.count('0', start, end) != s.count('1', start, end):
                return False

            mid = start + (end - start) // 2
            for i in range(start, mid):
                if s[i] != s[start]:
                    return False

            for i in range(mid, end):
                if s[i] != s[end]:
                    return False

            return True

        length = len(s)

        if length <= 1:
            return 0

        max_win_sz = length if length % 2 == 0 else length - 1

        result = 0

        for win_sz in range(2, max_win_sz + 1, 2):
            for start in range(0, length - win_sz + 1):
                if is_valid(s, start, start + win_sz):
                    result += 1

        return result

s = Solution()
s.countBinarySubstrings('00110')