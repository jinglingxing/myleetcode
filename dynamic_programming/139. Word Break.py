#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:39:09 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                sub_str = s[j:i]
                if(sub_str in wordDict): 
                     if(dp[j] == True):
                        print(" string: " + s[j:i])
                        dp[i] = True
                        break
        return dp[-1]
                    
            
if __name__ == '__main__':
    sol = Solution()
    s = 'leetcode'
    wordDict = ['leet','code']
    sol.wordBreak(s,wordDict)
    