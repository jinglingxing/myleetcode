#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:33:29 2020

@author: jinlingxing
"""
'''
Write a function that reverses a string. The input string is given as an All kind of LIST of characters char[].

Do not allocate extra space for another All kind of LIST, you must do this by modifying the input All kind of LIST in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left<=right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left+=1
            right-=1