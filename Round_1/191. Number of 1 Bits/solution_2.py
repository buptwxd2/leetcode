# naive solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        num_bits = 0
        mask = 1

        for _ in range(32):
            if (n & mask) != 0:
                num_bits += 1
            mask = mask << 1

        return num_bits

"""
Results: 
Runtime: 24 ms, faster than 92.07% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.
"""