"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

input  output
123     741
456     852
789     963
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 123
        # 456
        # 789
        m = len(matrix)
        n = len(matrix[0])

        # exchange rows and cols
        # 147
        # 258
        # 369
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                # reverse each row
        # 741
        # 852
        # 963
        for i in range(m):
            matrix[i] = matrix[i][::-1]
