#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:34:04 2020

@author: jinlingxing
"""

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> int:
        #list[int] to str; list[int] to int
        int_digits = int(''.join(str(i) for i in digits))
        int_digits+=1
        #int to list[int]
        res = [int(x) for x in str(int_digits)]
        return res