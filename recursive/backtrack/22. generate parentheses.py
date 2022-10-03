#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:35:57 2020

@author: jinlingxing
"""
'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output_arr = []
        self.backtracking(output_arr, "", n, 0, 0)
        return output_arr
    
    def backtracking(self, output_arr: list, curr_arr: str, n: int, close: int, open: int):
        if (len(curr_arr) == n*2):
            output_arr.append(curr_arr)
            return 
        
        if (open < n):
            self.backtracking(output_arr, curr_arr+'(', n, close, open+1)
        if (close < open):
            self.backtracking(output_arr, curr_arr+')', n, close+1, open)


sol = Solution()
n = 2
sol.generateParenthesis(n)