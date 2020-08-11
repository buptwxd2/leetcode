class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        row = len(board)
        col = len(board[0])

        visited = [[False] * col for _ in range(row)]

        def bfs(m, n):
            nonlocal override
            nonlocal points

            queue = [(m, n)]
            visited[m][n] = True

            while queue:
                i, j = queue.pop(0)
                points.append([i, j])

                visited[i][j] = True
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    override = False

                # move up
                if i > 0 and board[i - 1][j] == 'O' and not visited[i - 1][j]:
                    queue.append((i - 1, j))
                    visited[i - 1][j] = True
                # move down
                if i < row - 1 and board[i + 1][j] == 'O' and not visited[i + 1][j]:
                    queue.append((i + 1, j))
                    visited[i + 1][j] = True
                # move left
                if j > 0 and board[i][j - 1] == 'O' and not visited[i][j - 1]:
                    queue.append((i, j - 1))
                    visited[i][j - 1] = True
                # move right
                if j < col - 1 and board[i][j + 1] == 'O' and not visited[i][j + 1]:
                    queue.append((i, j + 1))
                    visited[i][j + 1] = True

        def override_to_x(points, board):
            for x, y in points:
                board[x][y] = 'X'

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and not visited[i][j]:
                    override = True
                    points = []

                    bfs(i, j)
                    if override:
                        override_to_x(points, board)

        return

"""
Results:
Runtime: 180 ms, faster than 27.66% of Python3 online submissions for Surrounded Regions.
Memory Usage: 17.9 MB, less than 14.60% of Python3 online submissions for Surrounded Regions.
"""