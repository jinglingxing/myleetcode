#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:28:19 2020

@author: jinlingxing
"""

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, [False]*len(nums), [], ans)
        return ans
    
    def dfs(self, nums, used, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return 
        
        for i in range(0, len(nums)):
            if used[i]:
                continue
            if i>0 and not used[i-1] and nums[i] == nums[i-1]: #unique permutations
                continue
            used[i] = True
            curr.append(nums[i])
            self.dfs(nums, used, curr, ans)
            curr.pop()
            used[i] = False   
