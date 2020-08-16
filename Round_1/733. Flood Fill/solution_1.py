class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        row = len(image)
        col = len(image[0])

        points = []
        target = image[sr][sc]
        visited = {}

        def dfs(sr, sc):
            nonlocal points

            if sr < 0 or sr > row - 1:
                return

            if sc < 0 or sc > col - 1:
                return

            if image[sr][sc] != target:
                return

            if [sr, sc] not in points:
                points.append([sr, sc])
            else:
                return

            # move left:
            dfs(sr, sc - 1)

            # move right
            dfs(sr, sc + 1)

            # move up
            dfs(sr - 1, sc)

            # move down
            dfs(sr + 1, sc)

        dfs(sr, sc)

        def fillup_new_color(image, points, new_color):
            for x, y in points:
                image[x][y] = new_color

        new_image = image.copy()
        fillup_new_color(new_image, points, newColor)

        return new_image

"""
Results:
DFS using recursive way
"""