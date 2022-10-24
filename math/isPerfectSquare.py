#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:51:57 2020

@author: jinlingxing
"""

'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left<=right:
            mid = left+(right-left)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid+1
            else:
                right = mid-1
        return False