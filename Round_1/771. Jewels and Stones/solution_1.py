class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)

        count = 0

        for stone in S:
            if stone in jewels:
                count += 1

        return count


"""
Results:
Runtime: 24 ms, faster than 89.87% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
"""