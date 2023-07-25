#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:01:26 2020

@author: jinlingxing
"""

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # mark all the other islands adjacent to "grid[i][j]"" to be '0'  
        def removeIsland(i,j):
            if i+1 < len(grid) and grid[i+1][j] == '1':
                grid[i+1][j] = '0'
                # check the islands adjacent to "grid[i+1][j]""
                removeIsland(i+1, j)
            if i-1 >= 0 and grid[i-1][j] == '1':
                grid[i-1][j] = '0'
                removeIsland(i-1, j)
            if j+1 < len(grid[0]) and grid[i][j+1] == '1':
                grid[i][j+1] = '0'
                removeIsland(i, j+1)
            if j-1 >= 0 and grid[i][j-1] == '1':
                grid[i][j-1] = '0'
                removeIsland(i, j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # mark the island 'grid[i][j]' to '0'
                    grid[i][j] == '0'
                    # call removeIsland function to mark all the island near 'grid[i][j]' to be '0'
                    removeIsland(i,j)
                    count += 1
        return count