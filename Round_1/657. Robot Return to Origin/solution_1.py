class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt_dict = {'U': 0, 'D': 0,
                    'R': 0, 'L': 0}

        for move in moves:
            cnt_dict[move] = cnt_dict[move] + 1

        return cnt_dict['U'] == cnt_dict['D'] and cnt_dict['R'] == cnt_dict['L']

"""
Results:
Runtime: 56 ms, faster than 78.38% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 13.9 MB, less than 52.70% of Python3 online submissions for Robot Return to Origin.
"""