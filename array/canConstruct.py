#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:34:47 2020

@author: jinlingxing
"""

'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Using counter to count the number of unique chars in ransomNote and magazine. 
        #For example: ransomNote: 'abbcd', magazine: 'aabbbcc'. So, count(a) in ransomNote: 1, count(a) in magazine: 2, the if condition satisfied. But count(d) in ransomNote: 1, count(d) in magazine: 0, the if condition doesn't satisfied.
        ransom_set = set(ransomNote) #unique chars
        for i in ransom_set:
            if ransomNote.count(i)>magazine.count(i): 
                return False
        return True