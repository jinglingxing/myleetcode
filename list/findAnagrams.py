#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:20:16 2020

@author: jinlingxing
"""

'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

from collections import Counter
from typing import List
###this solution only works on small examples
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:

#         len_p = len(p)
#         res = []
#         for i in range(0,len(s)-len(p)+1):
#             part_sorted_s  = sorted(s[i:i+len_p])
#             if list(sorted(p)) == part_sorted_s:
#                 res.append(i)
#         return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        p1 = Counter(p)
        res = []
        for i in range(0,len(s)-len(p)+1):
            part_s  = Counter(s[i:i+len_p])
            if part_s == p1:
                res.append(i)
        return res
    
sol = Solution()
s= "cbaebabacd" 
p= "abc"
sol.findAnagrams(s,p)

if a in b:
    return True


