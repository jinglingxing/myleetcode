#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:39:35 2020

@author: jinlingxing
"""
from typing import List        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums[0],nums[1])
        if(len(nums) == 3):
            return max(nums[0],nums[1],nums[2])
        
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp1 = [0]*(len(nums))
        dp1[1] = nums[1]
        dp1[2] = max(nums[1],nums[2])
              
        for i in range(2,len(nums)-1): #don't consider the last value
            dp[i] = max(dp[i], dp[i-2]+nums[i],dp[i-1])
               
        for j in range(3,len(nums)): #don't consider the first value
            dp1[j] = max(dp1[j], dp1[j-2]+nums[j],dp1[j-1])
        return max(max(dp),max(dp1))        
        
        
if __name__ == "__main__":
    sol = Solution()
#    nums = [1,3,1,3,100]
    nums = [2,7,9,3,1]
    sol.rob(nums)