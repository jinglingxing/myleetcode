#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:02:45 2020

@author: jinlingxing & luc michea
"""
'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True
Note:

The string size will be in the range [1, 100].
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack "stars": save "(" index 
        # stack "opens": save '*' index
        stars = []
        opens = []
        for i, char in enumerate(s):
            if char == '(':
                opens.append(i)
            elif char == '*':
                stars.append(i)
            else:
                # When meet ")", first try pop from stack "opens" because * can use for several ways;                     otherwise pop from stack "stars".
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        # if stack stars and opens are not empty, we need to pop them to check if "*" can represent ")"
        while stars and opens:
            # we need to make sure we don't have **(( cases, so we need to add a if condition to check elements in stack "stars" are behind elements in the stack "opens"
            if stars[-1] > opens[-1]:
                stars.pop()
                opens.pop()
            else:
                break
        return len(opens) == 0
sol = Solution()
s = "(*)("
sol.checkValidString(s)


