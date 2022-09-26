#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:48:48 2020

@author: jinlingxing & luc michea
"""

'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
import numpy as np
from typing import List
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res =  [1] * len(nums)
#         new_nums = np.array(nums)
#         for i in range(0,len(nums)):
#             res = [nums[i]*j for j in res[0:i]] + [res[i]] + [nums[i]*j for j in res[i+1:]]
#         return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = np.ones(len(nums), dtype = int)
        right = np.ones(len(nums), dtype = int)   
        prod = np.ones(len(nums), dtype = int)
        
        for i in range(0,len(nums)-1):
            left[i+1] = left[i]*nums[i]
        nums.reverse()
        for j in range(0,len(nums)-1):
            right[j+1] = right[j]*nums[j]
        for k in range(0,len(nums)):
            prod[k] = left[k]*right[len(nums)-k-1]
        return prod
sol = Solution()
nums = [1,2,3,4]
sol.productExceptSelf(nums)