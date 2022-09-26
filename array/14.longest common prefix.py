#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:34:15 2020

@author: jinlingxing
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ''
        for i in range(0,len(strs[0])):
            c = strs[0][i]
            for j in range(0, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c: # if we don't add i == len(strs[j]), the case ["aa","a"] will cause index of bound problem
                    return strs[0][0:i]
        return strs[0]