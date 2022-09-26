#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:00:52 2020

@author: jinlingxing
"""

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        K = self.kadane(A)
        CS = sum(A)
        for i in range(len(A)):
            A[i] = -A[i]
        CS = CS+ self.kadane(A)
        if CS>K and CS!=0:
            return CS
        else:
            return K
    def kadane(self, nums):
        if len(nums)>1:
            dp = [nums[0]]*len(nums)
            for i in range(1, len(nums)):
                dp[i] = max(dp[i-1]+nums[i], nums[i])
            return max(dp)
        else:
            return nums[0]