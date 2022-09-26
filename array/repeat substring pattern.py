#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:05:21 2020

@author: jinlingxing
"""
'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        k = 1
        while k <= len(s)//2:
            sub = s[0:k]
            reminder = len(s)%k
            if not reminder:
                if sub * int(len(s)//k) == s:
                    return True
            k+=1
        return False
            