#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:09:19 2020

@author: jinlingxing
"""



from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==0):
            print(0)
            return 0
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
  
        if(nums[1]>=nums[0]):
            dp[1] = nums[1]
            print(dp[1])
        else:
            dp[1] = nums[0]
        
        if(len(nums)>2):   
            for i in range(2,len(nums)):
                dp[i] = max(dp[i], dp[i-2]+nums[i],dp[i-1])
                print(dp[i])
        return dp[-1]
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1,1]
    sol.rob(nums)