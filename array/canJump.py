#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:52:31 2020

@author: jinlingxing
"""

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndexPostion = len(nums)-1
        for i in range(lastGoodIndexPostion, -1, -1):
            if(i+nums[i] >= lastGoodIndexPostion):
                lastGoodIndexPostion = i
        return lastGoodIndexPostion==0

        
sol = Solution()
nums = [2,3,1,1,4]
sol.canJump(nums)