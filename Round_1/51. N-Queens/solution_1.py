class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []

        def backtrack(pos, row):
            if len(pos) == n:
                sols.append(pos)
            for col in range(n):
                if all(row != row1 and col != col1 and abs(row - row1) != abs(col - col1)
                       for row1, col1 in pos):
                    backtrack(pos + [(row, col)], row + 1)

        backtrack([], 0)

        return [
            [''.join('Q' if (i, j) in sol else '.' for i in range(n)) for j in range(n)]
            for sol in sols
        ]

"""
Results:
Back Tracking Way
Runtime: 128 ms, faster than 39.29% of Python3 online submissions for N-Queens.
Memory Usage: 14.2 MB, less than 41.87% of Python3 online submissions for N-Queens.
"""