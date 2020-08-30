class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

"""
Results:
Runtime: 36 ms, faster than 93.94% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 13.9 MB, less than 41.78% of Python3 online submissions for Robot Return to Origin.
"""