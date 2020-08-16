class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        row = len(image)
        col = len(image[0])

        points = []
        target = image[sr][sc]

        def bfs(sr, sc):
            queue = []
            queue.append([sr, sc])

            while queue:
                curr_x, curr_y = queue.pop(0)
                points.append([curr_x, curr_y])

                # left
                if curr_y > 0 and image[curr_x][curr_y - 1] == target and [curr_x, curr_y - 1] not in points:
                    queue.append([curr_x, curr_y - 1])

                # right:
                if curr_y < col - 1 and image[curr_x][curr_y + 1] == target and [curr_x, curr_y + 1] not in points:
                    queue.append([curr_x, curr_y + 1])

                # up
                if curr_x > 0 and image[curr_x - 1][curr_y] == target and [curr_x - 1, curr_y] not in points:
                    queue.append([curr_x - 1, curr_y])

                # down
                if curr_x < row - 1 and image[curr_x + 1][curr_y] == target and [curr_x + 1, curr_y] not in points:
                    queue.append([curr_x + 1, curr_y])

        def fillup_new_color(image, points, new_color):
            for x, y in points:
                image[x][y] = new_color

        bfs(sr, sc)
        fillup_new_color(image, points, newColor)

        return image

"""
Results:
BFS
Runtime: 80 ms, faster than 74.26% of Python3 online submissions for Flood Fill.
Memory Usage: 14 MB, less than 43.37% of Python3 online submissions for Flood Fill.
"""