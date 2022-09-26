#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:15:45 2020

@author: jinlingxing
"""

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        count = 0
        while z!=0:
            if z & 1 == 1:
                count+=1
            z>>=1
        return count
    
sol = Solution()
x = 1
y = 4
sol.hammingDistance(x, y)