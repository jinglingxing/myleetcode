#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:11:47 2020

@author: jinlingxing
"""

'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        shift = 0
        
        while m != n:
            
            m = m >> 1
            n = n >> 1
        
            shift += 1
        
        
        return m << shift

sol = Solution()
m = 10
n = 12
sol.rangeBitwiseAnd(m, n)