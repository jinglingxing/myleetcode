#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:25:18 2020

@author: jinlingxing
"""

'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
'''

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         dic = {}
#         for i in range(0, len(s)):
#             dic[s[i]] = i
        
#         for j in t:
#             if j not in dic:
#                 #t.replace('j', '') 
#                 idx = t.index(j)
#                 t = t[:idx] + t[idx+1:]
#         return s == t
    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0 :
            return True
        for j in range(len(t)):
            if s[i] == t[j]:
                i+=1
            if i == len(s):
                return True
        return False
    
sol = Solution()
s = 'abc'
t = 'ahbgdc'
sol.isSubsequence(s, t)