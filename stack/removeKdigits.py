#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:13:58 2020

@author: jinlingxing
"""

'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
class Solution:           
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for each in num:   
            # Pop element from stack if the current element is smaller than last added element in stack
            while k and stack and stack[-1]>each:
                stack.pop()
                k -= 1
            stack.append(each)

        # If still k elements left to remove, then remove them from the stack. num = '9', k = 1
        while k>0:
            stack.pop()
            k -= 1
        #Remove leading zeros
        output = "".join(stack).lstrip("0")

        return (output if output else "0")
            
sol = Solution()
num = '34'
k = 1
sol.removeKdigits(num, k)