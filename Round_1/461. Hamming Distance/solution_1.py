class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y  # bitwise exclusive or

        num_of_1 = 0

        while z:
            z = z & (z - 1)  # bitwise and
            num_of_1 += 1

        return num_of_1

"""
Results:
Runtime: 24 ms, faster than 86.19% of Python3 online submissions for Hamming Distance.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Hamming Distance.
"""