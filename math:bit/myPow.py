#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:52:20 2020

@author: jinlingxing
"""

'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n<0:
            n = abs(n)
            x = 1/x
            
        while n>0:
            if n&1:
                res = res * x
            if res ==0:
                return res
            x *= x
            n>>=1
        return res

    
sol = Solution()
x=2
n=5
sol.myPow(x,n)