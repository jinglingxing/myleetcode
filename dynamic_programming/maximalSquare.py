#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:46:37 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: #matrix = []
            return 0
        rows = len(matrix)+1
        cols = len(matrix[0])+1
        dp = [[0 for i in range(cols)] for j in range(rows)]
        max_len = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    max_len = max(max_len, dp[i][j])
        return max_len*max_len
    
sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol.maximalSquare(matrix)
