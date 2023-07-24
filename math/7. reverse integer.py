#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:50:35 2020

@author: jinlingxing
"""

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        str_x = str(abs(x))
        reverse_str_x = str_x[::-1]
        reverse_int_x = int(reverse_str_x)

        result = -reverse_int_x if x < 0 else reverse_int_x

        return result if result <= MAX_INT and result >= MIN_INT else 0


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        x1 = abs(x)
        while x1 != 0:
            pop = x1 % 10
            x1 //= 10  # x/=10 ---> 123/=10 ---> 12.3
            temp = rev*10 + pop
            if -2**31 < temp < 2**31-1:
                rev = temp
            else:
                return 0
        if x > 0:
            return rev
        else:
            return -rev

