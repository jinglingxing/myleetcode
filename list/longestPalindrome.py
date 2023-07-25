#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:08:27 2020

@author: jinlingxing
"""
class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        def expandFromMiddle(s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expandFromMiddle(s,i,i)
            len2 = expandFromMiddle(s,i,i+1)
            cur = max(len1,len2)
            if(cur > end - start):
                start = i-(cur-1)//2
                end = i+cur//2
        return s[start:end+1]

        

if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    sol.longestPalindrome(s)