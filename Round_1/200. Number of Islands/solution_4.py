class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        visited = [[False] * col for _ in range(row)]

        def bfs(m, n):
            queue = [(m, n)]
            visited[m][n] = True

            while queue:
                i, j = queue.pop(0)

                visited[i][j] = True

                # move up
                if i > 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
                    queue.append((i - 1, j))
                    visited[i-1][j] = True
                # move down
                if i < row - 1 and grid[i + 1][j] == '1' and not visited[i + 1][j]:
                    queue.append((i + 1, j))
                    visited[i+1][j] = True
                # move left
                if j > 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
                    queue.append((i, j - 1))
                    visited[i][j-1] = True
                # move right
                if j < col - 1 and grid[i][j + 1] == '1' and not visited[i][j + 1]:
                    queue.append((i, j + 1))
                    visited[i][j+1] = True

        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    bfs(i, j)

        return cnt

"""
BFS way
Runtime: 132 ms, faster than 96.66% of Python3 online submissions for Number of Islands.
Memory Usage: 14.6 MB, less than 98.22% of Python3 online submissions for Number of Islands.
"""