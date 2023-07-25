#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:10:33 2020

@author: jinlingxing
"""

'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        s=[i for i in s]
        l=["a","e","i","o","u","A","E","I","O","U"]
        while left<right:
            if s[left] in l:
                if s[right] in l:
                    s[left],s[right]=s[right],s[left]
                    left,right=left+1,right-1
                else:
                    right-=1
            else:
                left+=1
        return "".join(s)