#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:58:09 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0]=1
        if(len(nums) == 0):
            return 0
        for i in range(0,target+1):        
            for n in range(0,len(nums)):
                if(i>=nums[n]):
                    dp[i] = dp[i] + dp[i-nums[n]]
                    print("dp[nums[n]]", + dp[nums[n]]) 
                    
                    
        print(dp[-1])
        return dp[-1]
        
        
        
if __name__ == '__main__':
    sol = Solution()
#    nums = [9]
#    target = 3
    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    sol.combinationSum4(nums, target)