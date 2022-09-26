#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:13:15 2020

@author: jinlingxing
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        dp = [0]*(len(s)+1)
        dp[0]=1
        if(int(s[0]) == 0):
            dp[1]=0
        else:
            dp[1]=1
            
        for i in range(2, len(s)+1):
            if(1 <= int(s[i-1:i]) <= 9):
                dp[i] = dp[i] + dp[i-1]
            if(10 <= int(s[i-2:i]) <= 26):
                dp[i] = dp[i] + dp[i-2]
        return dp[-1]
        
            
   

if __name__ == '__main__':
    sol = Solution()
    s = "2263"
    sol.numDecodings(s)