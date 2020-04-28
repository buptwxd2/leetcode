class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)

        count = 0

        return sum(S.count(jewel) for jewel in jewels)


"""
Results:
Runtime: 20 ms, faster than 97.68% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
"""