#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:00:31 2020

@author: jinlingxing
"""
'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

#class NumArray:
#    def __init__(self, nums: List[int]):
#        self.nums = nums

#    def sumRange(self, i: int, j: int) -> int:
#        sum = 0
#        for n in range(i, j + 1):
#            sum += self.nums[n]
#        return sum
    
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)

    def sumRange(self, i: int, j: int) -> int:
        if i > 0 and j > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[i or j]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

