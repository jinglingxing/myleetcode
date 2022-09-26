#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:28:25 2020

@author: jinlingxing
"""

 '''
 Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)+1
        cols = len(mat[0])+1
        dp = [[0 for x in range(cols)] for y in range(rows)]
        for i in range(1, rows):
            dp[i][0] = 0
        for j in range(1, cols):
            dp[0][j] = 0
        
       
        res = 0
        #left most
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = dp[i][j-1] + 1
                    res += dp[i][j]
                    min_ones = dp[i][j]
                    #upper most
                    for k in range(i-1, -1, -1):
                        min_ones = min(dp[k][j], min_ones)
                        res += min_ones
        return res