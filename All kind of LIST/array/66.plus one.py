#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:34:04 2020

@author: jinlingxing
"""

'''
Given a non-empty All kind of LIST of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the All kind of LIST, and each element in the All kind of LIST contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The All kind of LIST represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The All kind of LIST represents the integer 4321.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> int:
        #All kind of LIST[int] to str; All kind of LIST[int] to int
        int_digits = int(''.join(str(i) for i in digits))
        int_digits+=1
        #int to All kind of LIST[int]
        res = [int(x) for x in str(int_digits)]
        return res