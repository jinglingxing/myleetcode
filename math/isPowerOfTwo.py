#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:21:03 2020

@author: jinlingxing
"""
'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n >0:
            if n&1 == 1:
                count+=1
            n>>=1
        return count==1