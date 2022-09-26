#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:28:14 2020

@author: jinlingxing
"""

'''
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
'''

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic = {}
        for t in T:
            if t not in dic:
                dic[t] = 1
            else:
                dic[t] += 1
        res = ''      
        for i in range(0,len(S)):
            if S[i] in dic:
                res += S[i] * dic[S[i]]
                dic[S[i]] = 0 
        
        for key, value in dic.items():
            if value != 0:
                res += key * dic[key]
        
        return res