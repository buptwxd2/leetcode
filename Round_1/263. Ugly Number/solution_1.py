class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        if num == 1:
            return True

        test_factors = [2, 3, 5]

        tmp = num

        for factor in test_factors:
            while tmp % factor == 0:
                tmp = tmp / factor

        return tmp == 1

"""
Results:
Runtime: 24 ms, faster than 93.09% of Python3 online submissions for Ugly Number.
Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Ugly Number.
"""