#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:09:19 2020

@author: jinlingxing
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums) == 1:
            return nums[0]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # test case: [1, 51, 2]
            dp[i] = max(max(dp), dp[i-2] + nums[i])

        return dp[-1]
        
        
