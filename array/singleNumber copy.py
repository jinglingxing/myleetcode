#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:40:15 2020

@author: jinlingxing
"""
'''
Given a non-empty array of integers, every element appears three times except
 for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement 
it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 1:
            for i in range(0, len(nums)-2, 3):
                if nums[i] != nums[i+2]:
                    return nums[i]
            return nums[len(nums)-1]
            
        else:
            return nums[0]
        
sol = Solution()
nums = [0,1,0,1,0,1,99]
sol.singleNumber(nums)
        