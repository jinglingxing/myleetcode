#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:24:53 2020

@author: jinlingxing
"""

'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')               
        res = []
        for i in range(len(s)-1, -1, -1):
            if len(s[i]) >0:   
                res.append(s[i])
        
        return ' '.join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        # remove leading and ending space
        no_leading_space_string = s.strip()  # " hello word "
        split_string = no_leading_space_string.split(' ')
        split_string = [x for x in split_string if x]
        return " ".join(split_string[::-1])