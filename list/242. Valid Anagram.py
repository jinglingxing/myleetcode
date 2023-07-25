#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:07:10 2020

@author: jinlingxing
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if(len(s)!=len(t)):
            return False
        count = 0    
        for i in range(0,len(s)):
            if(s[i] == t[i]):
                count += 0 
                print(count)
            else:
                count += 1
                print(count)
        if(count == 0):
            return True
        else: 
            return False

if __name__ == '__main__':
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    sol.isAnagram(s,t)