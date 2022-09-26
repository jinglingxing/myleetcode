#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:32:25 2020

@author: jinlingxing
"""
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #left scan
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        # if it does not appear, return [-1, -1] early.
        else:
            return [-1,-1]
            
        #right scan
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                right_idx = i
                break
                
        return [left_idx, right_idx]
        
    
sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
sol.searchRange(nums, target)