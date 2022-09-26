#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:05:30 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndexPosition = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if(i+nums[i]>=lastGoodIndexPosition):
                lastGoodIndexPosition = i
        return lastGoodIndexPosition == 0
        
        

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    sol.canJump(nums)