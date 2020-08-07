class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or i > row - 1:
                return

            if j < 0 or j > col - 1:
                return

            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)

        return cnt

