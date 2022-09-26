#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:20 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem :
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Example 1:S
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
'''

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = True
            else:
                res.pop(i)
        return list(res.keys()).pop()
    
    
if __name__=='__main__':
    sol = Solution()
    inp = [2,2,1]
    out = sol.singleNumber(inp)
    print("The solution to {} is : {}".format(inp, out))
    
    
'''
We could have also used the XOR operator as : a XOR a = 0 and b XOR 0 = b
(Best answer from a friend)
Hence :
   def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res 
'''    
