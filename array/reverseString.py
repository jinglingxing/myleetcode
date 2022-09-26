#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:55:54 2020

@author: jinlingxing
"""
'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

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
        a_pointer = 0
        b_pointer = len(s)-1
        while a_pointer <= b_pointer:
            temp = s[a_pointer] 
            s[a_pointer] = s[b_pointer]
            s[b_pointer] = temp
            a_pointer+=1
            b_pointer-=1