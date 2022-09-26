#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:34:28 2020

@author: jinlingxing
"""
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2':['a','b','c'],
              '3':['d','e','f'],
              '4':['g','h','i'],
              '5':['j','k','l'],
              '6':['m','n','o'],
              '7':['p','q','r','s'],
              '8':['t','u','v'],
              '9':['w','x','y','z']}
        self.res = []
        combination = ''
        if digits:
            self.backtrack(combination, digits)
        return self.res
    def backtrack(self, combination, next_digits):
        #if there is no more digits to check
        if(len(next_digits) == 0):
            #the combination is done
            self.res.append(combination)
        #if there are still digits to check
        else:
            #iterate over all letters which map
            #the next available digit
            for i in self.dic[next_digits[0]]:
                self.backtrack(combination+i, next_digits[1:])
                
sol = Solution()
digits = '23'
sol.letterCombinations(digits)              
            