#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:25:49 2020

@author: jinlingxing
"""
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>2:
            if nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return nums[0]
            if len(nums)==1:
                return nums[0]