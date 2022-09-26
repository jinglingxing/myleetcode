#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:43:07 2020

@author: jinlingxing
"""
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
            
sol = Solution()
s = "dddccdbba"
sol.firstUniqChar(s)