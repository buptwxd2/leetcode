class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # define a matrix to store the optimals
        row = len(dungeon)
        col = len(dungeon[0])

        my_nums = [[float('inf')] * col for _ in range(row)]
        # need to walk from right-bottom to left-up
        my_nums[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # initialize the last row
        for j in range(col - 2, -1, -1):
            my_nums[-1][j] = max(1, my_nums[-1][j + 1] - dungeon[-1][j])

        # initialize the last column
        for i in range(row - 2, -1, -1):
            my_nums[i][-1] = max(1, my_nums[i + 1][-1] - dungeon[i][-1])

        # DP way to update
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                my_nums[i][j] = max(min(my_nums[i + 1][j], my_nums[i][j + 1]) - dungeon[i][j], 1)

        return my_nums[0][0]


"""
Results:
Use DP way
Runtime: 108 ms, faster than 9.37% of Python3 online submissions for Dungeon Game.
Memory Usage: 14.7 MB, less than 76.83% of Python3 online submissions for Dungeon Game.
"""