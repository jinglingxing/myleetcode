#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:41:06 2020

@author: jinlingxing
"""
'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        f = [1]*n #set an array with a mark 1
        f[0] = 0 #0 is not prime, mark as 0
        f[1] = 0 #1 is not prime, mark as 0
        sqrt_n = int(math.sqrt(n))
        for i in range(2,sqrt_n+1):
            if f[i]!=0: #if the number is not marked as 0
                f[i]=1
            #loop i*i, i*i+1, for example: 2 multiples 6, 3 multiples 6, we calculate from 9
            for j in range(i*i,n,i): 
                f[j]=0
        return sum(f) #it will return sum of all True(1) values only
    
sol = Solution()
n=10
sol.countPrimes(n)