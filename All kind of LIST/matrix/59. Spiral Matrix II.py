"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # n=3
        # create an empty matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1

        while left <= right and top <= bottom:
            # [[1,2,3], [0,0,0], [0,0,0]], top=1
            # top=1, right=1, bottom=1, left=1, matrix[1][1]=9, [[1,2,3], [0,0,4], [7,6,5]], top=2, while loop ended
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # [[1,2,3], [0,0,4], [0,0,5]], top=1, right=1
            # top, left, right, bottom: 2,1,1,1
            for i in range(top, bottom + 1):
                # i=1, right=2
                # i=2, right=2
                matrix[i][right] = num
                num += 1
            right -= 1

            # top=1, bottom=2, right=1
            # [[1,2,3], [0,0,4], [7,6,5]]
            # top=1, bottom=1
            # [[1,2,3], [0,0,4], [7,6,5]]
            if top <= bottom:
                # moving from right to left
                # bottom=2, i=1, num=6
                # bottom=2, i=0, num=7
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # left = 0, right = 1
            # i=1, top=1, matrix[1][0]=8 [[1,2,3], [8,0,4], [7,6,5]], left = 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix

