#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:12:02 2020

@author: jinlingxing
"""
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        #The ord() function returns an integer representing the Unicode character.
        res = 0
        for i in s:
            res = res*26 + ord(i) -64 #ord('A') = 65, ord('A')-64 = 1
        return res
        
    
    
    