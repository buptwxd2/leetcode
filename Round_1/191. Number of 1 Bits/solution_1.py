# naive solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n != 0:
            if n %2 != 0:
                num += 1
            n = n >> 1

        return num

"""
Results: 
Runtime: 32 ms, faster than 40.66% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.
"""