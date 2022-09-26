#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:46:34 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem:
    Given an integer array nums, find the contiguous subarray 
    (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) > 0:
            dp = [nums[0]]*len(nums)
            for i in range(1, len(nums)):
                dp[i] = max(dp[i-1]+nums[i], nums[i])
            return max(dp)
        
if __name__=='__main__':          
    sol = Solution()
    inp = [-2,1,-3,4,-1,2,1,-5,4]
    out = sol.maxSubArray(inp)
    print("The solution to {} is : {}".format(inp, out))