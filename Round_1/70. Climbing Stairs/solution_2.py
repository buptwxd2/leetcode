import functools


class Solution:

    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


"""
Results:
Runtime: 24 ms, faster than 83.95% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""