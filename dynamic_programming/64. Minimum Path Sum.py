#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:26:08 2020

@author: jinlingxing
"""

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns =  len(grid[0])
        dp = [[0 for x in range(columns)] for y in range(rows)]       
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, columns):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        # dp[0][1] = grid[0][0] + grid[0][1]
        # dp[1][0] = grid[0][0] + grid[1][0]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
sol.minPathSum(grid)