class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs version
        if not grid:
            return 0

        def dfs(grid, row, col):
            # mark current point as visited
            grid[row][col] = '*'  # any char other than '1'

            # move right
            if col < col_num - 1 and grid[row][col + 1] == '1':
                dfs(grid, row, col + 1)

            # move left:
            if col > 0 and grid[row][col - 1] == '1':
                dfs(grid, row, col - 1)

            # move down
            if row < row_num - 1 and grid[row + 1][col] == '1':
                dfs(grid, row + 1, col)

            # move up
            if row > 0 and grid[row - 1][col] == '1':
                dfs(grid, row - 1, col)

        row_num = len(grid)
        col_num = len(grid[0])
        count = 0

        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count

"""
Results:
Solve it using DFS way
Runtime: 128 ms, faster than 97.41% of Python3 online submissions for Number of Islands.
Memory Usage: 15 MB, less than 41.92% of Python3 online submissions for Number of Islands.
"""