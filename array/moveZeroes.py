#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:39:24 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem :
    Given an array nums, write a function to move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements.
    
Example : 
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
'''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 0:
            if(nums[i] == 0):
                nums.pop(i)
                nums.append(0)
            i-=1
        return nums


if __name__=='__main__':           
    sol = Solution()
    inp = [0,0,1,2,0,12]
    nums = inp.copy()
    out = sol.moveZeroes(nums)
    print("The solution to {} is : {}".format(inp, out))