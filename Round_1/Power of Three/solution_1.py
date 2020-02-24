class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        m = n
        while m != 1:
            if m % 3 != 0:
                return False
            else:
                m = m / 3

        return True