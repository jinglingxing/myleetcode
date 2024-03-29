#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:23:57 2020

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
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        an_integer += 1 
        return [int(x) for x in str(an_integer)]