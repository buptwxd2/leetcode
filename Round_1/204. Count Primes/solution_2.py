class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        my_list = [True] * n  # 0 to n-1
        my_list[0] = False  # 0 is not prime
        my_list[1] = False  # 1 is not prime

        for i in range(2, n):
            if my_list[i]:  # i is prime
                for j in range(2 * i, n, i):    # change start from 2*i to i*2, and that's solution_3
                    my_list[j] = False
            else:
                continue

        return len([x for x in my_list if x])


"""
Results: Runtime: 684 ms, faster than 46.74% of Python3 online submissions for Count Primes.
Memory Usage: 25.1 MB, less than 79.31% of Python3 online submissions for Count Primes.
Time complexity: O(n * log(log n)) according to the below wiki
wiki: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


