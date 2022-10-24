#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:28:42 2020

@author: jinlingxing
"""
class Solution:  
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        #8%2=0,4%2=0,2%2=0,1%2=1, return 1==1, ture
        #7%2=1, while loop broke, return 7==1, false
        while n%2 == 0: 
            n = n//2
        return n==1
        
sol = Solution()
n = 3
sol.isPowerOfTwo(n)
