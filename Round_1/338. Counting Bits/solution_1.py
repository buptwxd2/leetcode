class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        results = [0] * (num + 1)
        for i in range(1, num + 1):
            results[i] = results[i // 2] + i % 2

        return results


"""
Reference: https://www.youtube.com/watch?v=awxaRgUB4Kw
Results:
Runtime: 72 ms, faster than 98.13% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 28.71% of Python3 online submissions for Counting Bits.
"""