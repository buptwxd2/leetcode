class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        # 返回值代表是岛屿否到达边界
        # 若岛屿到达边界，那么就不是封闭的小岛
        def dfs(i, j):
            if i < 0 or i > row - 1:
                return True

            if j < 0 or j > col - 1:
                return True

            if grid[i][j] != 0:
                return False

            grid[i][j] = 2

            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)

            return left or right or up or down

        cnt = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    if not dfs(i, j):
                        cnt += 1

        return cnt
