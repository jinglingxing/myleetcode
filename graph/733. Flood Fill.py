"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # image = [[1,1,1],
        #          [1,1,0],
        #          [1,0,1]],
        # sr = 1, sc = 1, color = 2

        rows = len(image)
        cols = len(image[0])
        starting_color = image[sr][sc]

        # when the starting pixel have the same value as color, no flood needed
        if color == image[sr][sc]:
            return image

        def dfs(r: int, c: int) -> None:
            """
            r: row
            c: column
            """
            # r=1, c=1, image[1][1]=2
            # r=0, c=1, image[0][1]=2, return none
            # r=1, c=0, image[1][0]=2, return none
            # r=2, c=1, image[2][1]=2, return none
            # r=1, c=2, image[1][2]=2, return
            if image[r][c] == starting_color:
                image[r][c] = color
                # move up
                if r >= 1: dfs(r-1, c)
                # move left
                if c >= 1: dfs(r, c-1)
                # move down
                if r+1 < rows: dfs(r+1, c)
                # move right
                if c+1 < cols: dfs(r, c+1)
            else:
                return

        dfs(sr, sc)
        return image