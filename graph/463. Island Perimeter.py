"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()

        def dfs(i: int, j: int) -> int:
            if (i, j) in vis and grid[i][j] == 1:
                return 0
            # outside of the grid on it's water
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            vis.add((i, j))

            # i=2, j=1, (2,2)=1, (3,1)=0, (2,0)=1, (1,1)=0
            # i=0, j=1, (0,2)=1, (1,1)=0, (0,0)=1, (-1,1)=1
            perimeter = dfs(i, j + 1)  # moving right
            perimeter += dfs(i + 1, j)  # moving down
            perimeter += dfs(i, j - 1)  # moving left
            perimeter += dfs(i - 1, j)  # moving up
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         if len(grid) == 0 or len(grid[0]) == 0:
#             return 0
#         result = 0
#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[0])):
#                 if grid[i][j] == 1:
#                     result += 4
#                     if i > 0 and grid[i-1][j] == 1:
#                         result -= 2
#                     if j > 0 and grid[i][j-1] == 1:
#                         result -= 2
#         return result