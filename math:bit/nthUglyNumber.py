#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:16:13 2020

@author: jinlingxing
"""
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k = [0] * n
        t1 = t2 = t3 = 0
        k[0] = 1
        for i in range(1,n):
            k[i] = min(k[t1]*2,k[t2]*3,k[t3]*5)
            if(k[i] == k[t1]*2): t1 += 1
            if(k[i] == k[t2]*3): t2 += 1
            if(k[i] == k[t3]*5): t3 += 1
        return k[n-1] 