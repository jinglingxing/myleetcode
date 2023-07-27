"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return

            board[i][j] = '#'

            dfs(i - 1, j)  # move up
            dfs(i, j - 1)  # move left
            dfs(i + 1, j)  # move down
            dfs(i, j + 1)  # move right

        # mark all O's on the edges
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","#","X","X"]]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                # Change the edges 0 back
                elif board[i][j] == '#':
                    board[i][j] = 'O'