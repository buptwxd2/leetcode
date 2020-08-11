class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        row = len(board)
        col = len(board[0])
        visited = [[False] * col for _ in range(row)]

        def dfs(i, j):
            nonlocal override
            nonlocal points

            visited[i][j] = True
            points.append([i, j])
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                override = False

            if j > 0 and board[i][j - 1] == 'O' and not visited[i][j - 1]:
                dfs(i, j - 1)

            if j < col - 1 and board[i][j + 1] == 'O' and not visited[i][j + 1]:
                dfs(i, j + 1)

            if i > 0 and board[i - 1][j] == 'O' and not visited[i - 1][j]:
                dfs(i - 1, j)

            if i < row - 1 and board[i + 1][j] == 'O' and not visited[i + 1][j]:
                dfs(i + 1, j)

        def override_to_x(points, board):
            for x, y in points:
                board[x][y] = 'X'

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and not visited[i][j]:
                    override = True
                    points = []

                    dfs(i, j)
                    if override:
                        override_to_x(points, board)

        return

"""
Results:
Runtime: 196 ms, faster than 24.59% of Python3 online submissions for Surrounded Regions.
Memory Usage: 60.8 MB, less than 5.01% of Python3 online submissions for Surrounded Regions.
"""