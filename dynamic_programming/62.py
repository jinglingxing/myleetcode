#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:35:48 2020

@author: jinlingxing
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#        dp = [[0]*m,[0]*n] #two lists: one with 7 elements and one with 3 elements
        dp = [[0]*m]*n #three lists
        #        a = [[0 for x in range(columns)] for y in range(rows)]
        for i in range(m):
            dp[0][i] =1
        for j in range(n):
            dp[j][0] = 1
        if(m<=0|n<=0):
            return 0
            
        for i in range(1,n):
            for j in range(1,m):
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp[-1][-1])
        return dp[-1][-1]
        
if __name__ == "__main__":
    sol = Solution()
    m=7
    n=3
    sol.uniquePaths(m,n)