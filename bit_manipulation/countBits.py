#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:49:55 2020

@author: jinlingxing
"""

'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
#solution 1:
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(0,num+1):
            count = 0
            while i!=0:
                if i&1 == 1:
                    count+=1
                i>>=1
            res.append(count)
        return res
    
#solution 2:
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(0,num+1):
            res[i]= res[i//2] + i%2
        return res