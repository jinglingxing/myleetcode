#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:00:22 2020

@author: jinlingxing
"""

'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num ==0:
            return False
        while(num%4==0):
            num = num//4
        return num==1
