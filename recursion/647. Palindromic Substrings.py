#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:10:08 2020

@author: jinlingxing
"""

class Solution:

    def countSubstrings(self, s: str) -> int:
            
        def expandFromMiddle(s,l,r):
            count = 0
            while(l>=0 and r<len(s) and s[l] == s[r]):
                l-=1
                r+=1
                count+=1
            return count
        
        total = len(s)
        for i in range(1,len(s)):
            len1 = expandFromMiddle(s,i-1,i+1)
            len2 = expandFromMiddle(s,i-1,i)
            total += len1+len2
        return total
            
        

        
if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    sol.countSubstrings(s)