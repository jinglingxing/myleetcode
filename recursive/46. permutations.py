#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:05:42 2020

@author: jinlingxing
"""

'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [False]*len(nums), [], ans)
        return ans
    
    def dfs(self, nums, used, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return 
        
        for i in range(0, len(nums)):
            if used[i]:
                continue
            used[i] = True
            curr.append(nums[i])
            self.dfs(nums, used, curr, ans)
            curr.pop()
            used[i] = False