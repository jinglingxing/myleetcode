#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:15:10 2020

@author: jinlingxing
"""

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split()
        if len(new_s) >= 1:
            return len(new_s[-1])
        else:
            return 0