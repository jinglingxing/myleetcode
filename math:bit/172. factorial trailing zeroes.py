#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:20:34 2020

@author: jinlingxing
"""
#too slow
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         factorial = 1
#         for i in range(1, n+1):
#             factorial = factorial * i
#         str_f = str(factorial)
#         count = 0
        
#         for i in range(len(str_f)-1,-1,-1):
#             if str_f[i] == '0':
#                 count+=1
#             if str_f[i] != '0':
#                 return count

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n!=0:
            n = n//5
            count = count+n
        return count        
sol = Solution()
n=3
sol.trailingZeroes(n)