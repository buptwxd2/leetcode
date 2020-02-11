class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = int(self.reverse_str(str(x)))
        else:
            y = -1 * int(self.reverse_str(str(abs(x))))

        if -2 ** 31 <= y and y <= 2 ** 31 - 1:
            return y
        else:
            return 0

    def reverse_str(self, s):
        # s -> str
        # return reversed string of s
        s = list(s)
        s = s[::-1]
        s = ''.join(s)

        return s

