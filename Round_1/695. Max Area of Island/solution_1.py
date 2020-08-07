class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        row = len(grid)
        col = len(grid[0])

        visited = [[False] * col for _ in range(row)]

        def dfs(i, j):
            nonlocal max_area
            if i < 0 or i > row - 1:
                return 0

            if j < 0 or j > col - 1:
                return 0

            if not grid[i][j]:
                return 0

            if visited[i][j]:
                return 0

            visited[i][j] = True

            return 1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area