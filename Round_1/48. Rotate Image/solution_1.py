class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # this problem is split into two steps: transpose and then flip

        # 1. transpose it firstly
        N = len(matrix)  # note this is a square matrix
        for i in range(N):
            for j in range(i + 1, N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # 2. flip
        for i in range(N):
            for j in range(0, N // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][N - 1 - j]
                matrix[i][N - 1 - j] = tmp

        return


"""
Results:
Referred to https://www.youtube.com/watch?v=SA867FvqHrM
Split the rotate into two steps: 1.transpose 2. mirror vertically
Runtime: 32 ms, faster than 89.40% of Python3 online submissions for Rotate Image.
Memory Usage: 14 MB, less than 9.15% of Python3 online submissions for Rotate Image.
"""