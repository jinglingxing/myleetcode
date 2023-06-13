"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
"""

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(grid[0])):
                if row == self.find_column(j, grid):
                    result += 1
        return result

    @staticmethod
    def find_column(i: int, grid: List[List[int]]) -> int:
        res = []
        for row in grid:
            res.append(row[i])
        return res