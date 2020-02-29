import math


class Solution:
    def countPrimes(self, n: int) -> int:
        num = 0
        for i in range(1, n):
            if self.isPrime(i):
                print(i)
                num += 1

        return num

    def isPrime(self, m):
        if m == 1:
            return False

        if m == 2 or m == 3:
            return True

        for i in range(2, round(math.sqrt(m))+1):
            if m % i == 0:
                return False

        return True

s = Solution()
s.countPrimes(10)


"""
Results: Time Limit Exceeded
Time complexity: O(n ** 1.5)
"""


